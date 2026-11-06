class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                diff = (nums[i] + nums[left] + nums[right]) - target
                if abs(closest - target) > abs(diff):
                    closest = nums[i] + nums[left] + nums[right]
                if diff < 0:
                    left += 1
                elif diff > 0:
                    right -= 1
                else:
                    return closest
        return closest 
