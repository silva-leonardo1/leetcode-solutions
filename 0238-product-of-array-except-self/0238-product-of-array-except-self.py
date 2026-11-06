class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        sumP = [0] * len(nums)
        sumPrev = [0] * len(nums)
        res = [0] * len(nums)

        sumP[0], sumPrev[-1] = nums[0], nums[-1]

        for i in range(1, len(sumP), 1):
            sumP[i] = sumP[i-1] * nums[i]
        for j in range(len(sumPrev)-2, -1, -1):
            sumPrev[j] = sumPrev[j+1] * nums[j]

        for k in range(len(nums)):
            if k > 0 and k < len(nums) - 1:
                res[k] = sumP[k-1] * sumPrev[k+1]
            elif k == 0:
                res[k] = sumPrev[k+1]
            else:
                res[k] = sumP[k-1]
        return res
        