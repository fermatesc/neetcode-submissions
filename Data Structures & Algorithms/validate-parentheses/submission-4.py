class Solution:
    def isValid(self, s: str) -> bool:

        check = {'(': ')', '{': '}', '[' : ']'}

        stack = []
        for c in s:
            if c in check:
                stack.append(c)
            else:
                if not stack:
                    return False
                if check[stack[-1]] != c :
                    return False
                
                stack.pop()
        if stack:
            return False      
        return True