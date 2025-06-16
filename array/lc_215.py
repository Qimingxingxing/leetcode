sorting: nlogn
maxheap: klogn
minheap: nlogk

from heapq import *


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [-num for num in nums]
        heapify(nums)
        for i in range(k - 1):
            heappop(nums)
        return -nums[0]


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for i in range(len(nums)):
            heapq.heappush(h, nums[i])
            if len(h) > k:
                heapq.heappop(h)
        return h[0]


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def select(n, nums, start, end):
            if start == end:
                return nums[start]
            p = partition(nums, start, end)
            if n == p - start + 1:
                return nums[p]
            elif n < p - start + 1:
                return select(n, nums, start, p - 1)
            else:
                return select(n - p + start - 1, nums, p + 1, end)

        def partition(nums, start, end):
            i
            j
            # [3,2,1,4,6,5]

    pivot = nums[end]
    i = start - 1
    for j in range(start, end):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[end] = nums[end], nums[i + 1]
    return i + 1


return select(len(nums) - k + 1, nums, 0, len(nums) - 1)