def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        i = 0
        while i<=length:
            if nums[i] + nums[i+1] == target:
                return [i, i+1]
            