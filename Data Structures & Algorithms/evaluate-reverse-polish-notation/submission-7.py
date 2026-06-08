class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                b = stack.pop()
                a = stack.pop()
                exp = str(a) + token + str(b)
                stack.append(int(eval(exp)))
            else:
                stack.append(int(token))
        return stack[-1]     