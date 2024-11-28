class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        operator = '+' # Default operator
        s += '+'

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in '+-*/':
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(-num)
                elif operator == '*':
                    stack.append(stack.pop() * num)
                elif operator == '/':
                    stack.append(int(stack.pop() / num))
                operator = char
                num = 0
        return sum(stack)