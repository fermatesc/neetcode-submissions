class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c for c in s.lower() if c.isalnum()]
        if s == s[::-1]:
            return True
        return False