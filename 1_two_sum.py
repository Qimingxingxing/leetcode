class Solution:
    # brute force solution
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(l):
            for j in range(i+1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    # hashmap solution
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        map = {}
        for i in range(l):
            comp = target - nums[i]
            if comp in map:
                return [map[comp], i]
            map[nums[i]] = i
        return []
