class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = []
        res = [-1 for i in range(len(nums))]
        for i in range(len(nums)) * 2:
            while s and nums[i] > nums[s[-1]]:
                res[s.pop()] = nums[i]
            s.append(i)
        return res
