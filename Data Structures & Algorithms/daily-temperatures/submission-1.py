class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                j, topTemp = stack.pop()
                output[j] = i - j
            stack.append((i, temp))
        
        return output
