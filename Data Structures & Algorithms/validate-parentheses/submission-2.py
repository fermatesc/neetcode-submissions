class Solution:
    def isValid(self, s: str) -> bool:

        check = {'(': ')', '{': '}', '[' : ']'}

        stack = []
        for c in s:
            if c in check:
                stack.append(c)
            elif c in check.values():
                if not stack:
                    return False
                if check[stack[-1]] != c :
                    return False
                else:
                    stack.pop()
            else:
                return False  
        if stack:
            return False      
        return True