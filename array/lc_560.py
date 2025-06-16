# class Solution:
# def subarraySum(self, nums: List[int], k: int) -> int:
#     # prefix sum
#     # prefix sum + two sum
#     prefix = [0,1,2,3]

from collections import defaultdict


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        preSum = [0]
        temp = 0
        for num in nums:
            temp += num
            preSum.append(temp)

        d = defaultdict(int)
        for num in preSum:
            if num - k in d:
                res += d[(num - k)]
            d[num] += 1
        return res
        # sliding window

        # sorting

        # binary search

        # dp

        # two pointers