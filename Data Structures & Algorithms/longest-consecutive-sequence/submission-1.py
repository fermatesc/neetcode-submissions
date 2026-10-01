class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        
        for n in nums_set:
            if n-1 not in nums_set:
                count =1
                curr_n = n
                while curr_n +1 in nums_set:
                    curr_n +=1
                    count += 1
                max_len = max(max_len, count)

        return max_len