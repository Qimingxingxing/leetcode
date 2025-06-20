class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, j = 0, len(nums)-1
        k = 0
        while k <= j:
            if nums[k] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
            elif nums[k] == 0:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
                k += 1
            else:
                k += 1
