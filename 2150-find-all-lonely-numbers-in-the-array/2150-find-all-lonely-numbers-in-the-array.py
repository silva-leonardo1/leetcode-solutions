class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        ans = {}
        seen = set()

        for num in nums:
            ans[num] = num
            for n in (num, num - 1, num + 1):
                if n in seen:
                    ans.pop(n, None)
                    ans.pop(num, None)
            seen.add(num)
        return list(ans.keys())


