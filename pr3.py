def rearrange_by_frequency(nums: list[int]) -> list[int]:
    nums2 = {}
    for x in nums:
        if x not in nums2:
            nums2[x] = 1
        else:
            nums2[x] += + 1
    
    takrorlanmas_raqamlar = list(x for x in nums2)
    
    takrorlanmas_raqamlar.sort()

    takrorlanmas_raqamlar.sort(key=nums2.get, reverse=True)

    result = []
    for x in takrorlanmas_raqamlar:
        count = nums2[x]
        result.extend([x] * count)
    
    print(result)

rearrange_by_frequency([4, 5, 6, 5, 4, 3, 4])