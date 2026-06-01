class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(', '[', '{']
        closing = [')', ']', '}']
        map_c = {')' : '(', '}' : '{', ']' : '['}
        stack = []
        for char in s:
            if char in closing:
                if not stack or map_c[char] != stack[-1]:
                    return False
                stack.pop()
            elif char in opening:
                stack.append(char)

        if stack:
            return False
        
        return True