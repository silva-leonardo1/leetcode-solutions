class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        index = {}
        res = [-1] * len(nums1) 
        stack = []
        stack.append(nums2[0]) 
        for i, num in enumerate(nums1):
            index[num] = i
        for k in range(1, len(nums2), 1):
            if stack and stack[-1] > nums2[k]:
                stack.append(nums2[k])
            else:
                while stack and stack[-1] < nums2[k]:
                    if stack[-1] in index:
                        res[index[stack[-1]]] = nums2[k]
                    stack.pop(-1)
                stack.append(nums2[k])
        return res


