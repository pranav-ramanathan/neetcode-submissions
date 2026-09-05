from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        close_map = {")": "(", "}": "{", "]" : "["}
        stack = deque()
        for char in s:
            if char in close_map:
                if stack and close_map[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False
            