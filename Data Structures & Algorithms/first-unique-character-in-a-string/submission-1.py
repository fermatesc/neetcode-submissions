class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i, char in enumerate(s):
            if char not in seen:
                seen[char] = i
            else:
                seen[char] = float('inf')
        
        indexes = [i for i in seen.values() if i != float('inf')]
 
        return min(indexes) if indexes else -1