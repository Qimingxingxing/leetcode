class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        l = len(nums)
        temp = 1
        for i in range(l)[::-1]:
            res.append(temp)
            temp = temp * nums[i]
        prefix = 1
        res.reverse()
        for i in range(l):
            res[i] = res[i] * prefix
            prefix *= nums[i]
        return res
