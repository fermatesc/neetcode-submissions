class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        
        for n in nums_set:
            if n-1 not in nums_set:
                count =1
                while n +count in nums_set:
                    count += 1
                max_len = max(max_len, count)

        return max_len