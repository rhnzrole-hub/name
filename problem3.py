# Sonlar ro'yxatini chastotasiga qarab kamayish tartibida saralash. Chastotasi teng bo'lgan sonlar — qiymati bo'yicha o'sish tartibida joylashsin.

def rearrange_by_frequency(nums: list[int]) -> list[int]:
    counts = {}
    for x in nums:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    
    takrorlanmas_raqamlar = list(counts.keys())

    takrorlanmas_raqamlar.sort()
    
    takrorlanmas_raqamlar.sort(key=counts.get, reverse=True)
    
    result = []
    for x in takrorlanmas_raqamlar:
        soni = counts[x]
        result.extend([x] * soni)
        
    return result


print(rearrange_by_frequency([4, 5, 6, 5, 4, 3, 4]))