import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency = {}
        k_mostfrequent = [(0,0)] * k
        heapq.heapify(k_mostfrequent)

        for i in range(len(nums)):
            frequency[nums[i]] = frequency.get(nums[i], 0) + 1
            
        for k in range(len(nums)):
            x = frequency.pop(nums[k], None)
            if x is not None and x > k_mostfrequent[0][0]:
                heapq.heapreplace(k_mostfrequent, (x, nums[k]))

        return [m[1] for m in k_mostfrequent]