class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, val in enumerate(nums):
            for j, val2 in enumerate(nums[idx:]):
                if (idx != idx+j) and val+val2 == target:
                    return [idx, idx+j]