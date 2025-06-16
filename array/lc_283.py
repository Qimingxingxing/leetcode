class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        l = len(nums)
        for i in range(l):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
#    1 3 0 0
# # [0,1,0,3,12]