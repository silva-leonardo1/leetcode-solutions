class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        dic = {}
        left, right = 0, 0
        temp = 0
        while right < len(s):
            if s[right] in dic:
                left = max(left, dic[s[right]] + 1)
                count = max(count, temp)
                temp = right - left
            dic[s[right]] = right
            temp += 1
            right += 1
        return max(temp, count)