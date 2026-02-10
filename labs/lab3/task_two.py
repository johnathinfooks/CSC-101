
def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           # num:total ; 4:4, 9:13, 2:15, 1:16
    return total

result = tally([4, 9, 2, 1])

###########################################################

def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # idx:[new_list] ; 1:[4], 2:[4,9], 3:[4,9,2], 4:[4,9,2,1]
    return new_list

result = copy([4, 9, 2, 1])

###########################################################

def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # value:[new_list] ; 4:[5], 9:[5,10], 2:[5,10,3], 1:[5,10,3,2]
    return new_list

result = increment_all([4, 9, 2, 1])
