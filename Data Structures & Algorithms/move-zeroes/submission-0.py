class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        values = [ n for n in nums if n != 0]
        nums[:] = values + [ 0 for i in range(length-len(values))]
