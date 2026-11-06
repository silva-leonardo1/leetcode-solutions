class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        psum = [0] * len(nums)
        psum[0] = nums[0]
        seen = {0: 1}
        count = 0
        for i in range(1, len(nums), 1):
            psum[i] = psum[i-1] + nums[i]

        for j in range(len(psum)):
            diff = psum[j] - k
            if diff in seen:
                count+=seen.get(diff)
            elif psum[j] == k:
                count+=1
            seen[psum[j]] = seen.get(psum[j], 0) + 1
        return count