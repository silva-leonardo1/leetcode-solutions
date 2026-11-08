class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack = [0]
        res = [-1] * len(nums)
        for i in range(1, len(nums), 1):
            if stack and nums[stack[-1]] >= nums[i]:
                stack.append(i)
            elif stack and nums[stack[-1]] < nums[i]:
                while stack and nums[stack[-1]] < nums[i]:
                    print(stack)
                    res[stack[-1]] = nums[i]
                    stack.pop()
                stack.append(i)
        k = 0
        while k < len(nums):
            while nums[stack[-1]] < nums[k]:
                res[stack[-1]] = nums[k]
                stack.pop()
            k += 1
        return res