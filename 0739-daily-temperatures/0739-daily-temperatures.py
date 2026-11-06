class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        days = [0] * len(temperatures)
        stack = [0]
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while temp > temperatures[stack[-1]] and len(stack) > 1:
                days[stack[-1]] = i - stack[-1]
                stack.pop(-1)
            stack.append(i)
        return days