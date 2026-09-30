class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:     
        char_set = set()
        left = 0
        max_len = 0
        
        for right, c in enumerate(s):
            while c in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(c)

            max_len = max(max_len, right - left + 1)
            
        return max_len