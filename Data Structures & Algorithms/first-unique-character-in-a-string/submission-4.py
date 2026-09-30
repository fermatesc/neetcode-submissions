class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i, char in enumerate(s):
            if char not in seen:
                seen[char] = i
            else:
                seen[char] = -1
        
        for i in seen.values():
            if i != -1:
                return i

        return  -1