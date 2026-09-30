class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]
        for num in nums[:-1]:
            result.append(result[-1]*num)

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result