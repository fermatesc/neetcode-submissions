class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        numbers=[]
        for i, char in enumerate(tokens):
            if char not in operators:
                numbers.append(int(char))
            else:
                b = numbers.pop()
                a = numbers.pop()
                if char == "+":
                    numbers.append(a+b)
                elif char == "-":
                    numbers.append(a-b)
                elif char == "*":
                    numbers.append(a*b)
                elif char == "/":
                    numbers.append(int(a/b))

        return int(numbers[0])