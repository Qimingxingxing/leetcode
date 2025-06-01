class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        res = 0
        while l < r:
            lH, rH = height[l], height[r]
            if lH < rH:
                while l < r and height[l] <= lH:
                    res += lH - height[l]
                    l += 1
            else:
                while l < r and height[r] <= rH:
                    res += rH - height[r]
                    r -= 1
        return res
