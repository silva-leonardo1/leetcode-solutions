class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False
        nums.sort()
        aux = nums[0]
        count = 1
        
        for i in range(1, len(nums), 1):
            if nums[i] == aux:
                count += 1
                if count > 2:
                    return False
            else:
                count = 1
                aux = nums[i]
        return True

