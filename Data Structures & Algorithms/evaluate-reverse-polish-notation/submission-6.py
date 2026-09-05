from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda x, y: x + y, 
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y)
            }

        stack = deque()


        for token in tokens:
            if token in operations:
                op = token
                y, x = stack.pop(), stack.pop()
                stack.append(operations[op](x, y))
            else:
                stack.append(int(token))

        return stack.pop()
