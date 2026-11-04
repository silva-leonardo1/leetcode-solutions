class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        currentNum = nums[0]
        highestNum = float('inf')

        for i in range(len(nums)):
            if nums[i] < currentNum:
                currentNum = nums[i]
            
            elif nums[i] > currentNum:
                if nums[i] > highestNum:
                    return True
                    break
                else:
                    highestNum = nums[i]
        return False
            
