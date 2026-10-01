class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:     
        sub = set()
        max_count = 0
        l = 0
        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l+=1
            
            sub.add(s[r])
            max_count = max(max_count, r-l+1)

        return max_count