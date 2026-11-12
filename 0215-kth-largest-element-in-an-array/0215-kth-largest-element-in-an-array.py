import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        k_numbers = nums[:k]
        heapq.heapify(k_numbers)
        for i in range(k, len(nums), 1):
            if nums[i] > k_numbers[0]:
                heapq.heapreplace(k_numbers, nums[i])
        return k_numbers[0]