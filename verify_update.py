"""Check upgrade identity against the previously delivered signed APK."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile


def parse_metadata(badging, certificates):
    package = re.search(r"package: name='([^']+)' versionCode='(\d+)'", badging)
    signers = re.findall(r"Signer #\d+ certificate SHA-256 digest: ([0-9a-fA-F]{64})", certificates)
    if package is None or len(signers) != 1:
        raise ValueError("Expected one package and one APK signing certificate")
    return {"package": package[1], "version_code": int(package[2]), "signer_sha256": signers[0].lower()}


def apk_metadata(apk):
    tools = Path(os.environ["ANDROID_HOME"]) / "build-tools" / "36.0.0"
    badging = subprocess.check_output([str(tools / "aapt"), "dump", "badging", str(apk)], text=True)
    certificates = subprocess.check_output([str(tools / "apksigner"), "verify", "--print-certs", str(apk)], text=True)
    return parse_metadata(badging, certificates)


def validate_update(previous, current):
    if previous["package"] != "org.telegram.plus.beta" or current["package"] != previous["package"]:
        raise ValueError("Package differs from the previously delivered Telegram Plus APK")
    if current["signer_sha256"] != previous["signer_sha256"]:
        raise ValueError("Signing certificate differs: this APK cannot update the previous installation")
    if current["version_code"] <= previous["version_code"]:
        raise ValueError("Update version code must be higher than the previous APK")


def main():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", required=True)
    baseline = commands.add_parser("baseline")
    baseline.add_argument("--old-dir", type=Path, required=True)
    baseline.add_argument("--keystore", type=Path, required=True)
    baseline.add_argument("--output", type=Path, required=True)
    check = commands.add_parser("check")
    check.add_argument("--apk", type=Path, required=True)
    check.add_argument("--baseline", type=Path, required=True)
    check.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "baseline":
        apks = list(args.old_dir.rglob("*.apk"))
        if len(apks) != 1:
            raise ValueError("Expected exactly one previous APK")
        previous = apk_metadata(apks[0])
        if previous["package"] != "org.telegram.plus.beta":
            raise ValueError("Previous artifact is not the expected Telegram Plus package")
        with tempfile.TemporaryDirectory(prefix="telegram-plus-certificate-") as directory:
            certificate = Path(directory) / "certificate.der"
            # Read the store password from the environment; never put it in argv or output.
            subprocess.run([
                "keytool", "-exportcert", "-keystore", str(args.keystore),
                "-alias", os.environ["KEY_ALIAS"], "-storepass:env", "STORE_PASSWORD",
                "-file", str(certificate),
            ], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            digest = hashlib.sha256(certificate.read_bytes()).hexdigest()
        if digest != previous["signer_sha256"]:
            raise ValueError("Configured signing key does not match the previous APK; refusing incompatible build")
        args.output.write_text(json.dumps(previous, indent=2) + "\n")
        print("PASS: previous package verified; configured signing key matches the previous APK")
    else:
        previous = json.loads(args.baseline.read_text())
        current = apk_metadata(args.apk)
        validate_update(previous, current)
        args.report.write_text(
            "Update compatibility checks passed\n"
            f"Package: {current['package']}\n"
            f"Version code: {previous['version_code']} -> {current['version_code']}\n"
            f"Unchanged signing certificate SHA-256: {current['signer_sha256']}\n"
        )
        print("PASS: signed APK has the same package/certificate and a higher version code")


if __name__ == "__main__":
    main()
