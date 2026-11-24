class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        highest = 0

        for i in s:
            if i - 1 not in s:
                length = 1
                while i + length in s:
                    length += 1
                highest = max(length, highest)
        return highest