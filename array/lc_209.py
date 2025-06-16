class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        curSum = 0
        res = float("inf")
        j = 0
        for i in range(len(nums)):
            curSum += nums[i]
            while j <= i and curSum >= s:
                res = min(res, i - j + 1)
                curSum -= nums[j]
                j += 1
        return res if res != float("inf") else 0
