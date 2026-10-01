class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:     
        sub = set()
        max_count = 0
        l = 0
        mp={}
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]]+1, l)
            mp[s[r]]=r
            max_count = max(max_count, r-l+1)

        return max_count