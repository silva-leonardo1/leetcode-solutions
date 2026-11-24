class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res, path = [], []

        def backtrack(i, x):
            if i == k:
                res.append(path.copy())
                return
            if x > n:
                return
            path.append(x)
            backtrack(i+1, x+1)
            path.pop()

            backtrack(i, x+1)
        backtrack(0, 1)
        return res