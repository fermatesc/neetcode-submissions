class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        passed = []
        for i in nums:
            if i in passed:
                return True
            passed.append(i)
        return False