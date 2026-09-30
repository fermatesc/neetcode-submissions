class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, val in enumerate(nums):
            for j in range(len(nums[idx:])):
                if (idx != idx+j) and val+nums[idx+j] == target:
                    return [idx, idx+j]