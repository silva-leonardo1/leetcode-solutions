class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for k in range(len(nums) - 2):
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k - 1]:
                continue

            lowestNum = k + 1
            highestNum = len(nums) - 1

            while lowestNum < highestNum:
                diff = nums[k] + nums[lowestNum] + nums[highestNum]

                if diff < 0:
                    lowestNum += 1
                elif diff > 0:
                    highestNum -= 1
                else:
                    res.append([nums[k], nums[lowestNum], nums[highestNum]])
                    lowestNum += 1
                    highestNum -= 1
                    
                    while lowestNum < highestNum and nums[lowestNum] == nums[lowestNum - 1]:
                        lowestNum += 1

        return res