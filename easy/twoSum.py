def twoSum(nums: List[int], target: int) -> List[int]:
    length = len(nums)
    i = 0
    while i < length:
        j = i+1
        while j < length:
            if nums[i] + nums[j] == target:
                return [i, j]
            j += 1
        i += 1
        # j += 1 