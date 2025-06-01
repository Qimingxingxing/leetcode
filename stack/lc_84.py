class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        stack = [-1]
        maxArea = 0
        
        for i in range(len(heights)):
            curt = heights[i]
            while stack[-1] != -1 and curt <= heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                maxArea = max(maxArea, h * w)
            stack.append(i)
        while stack[-1] != -1:
            maxArea = max(maxArea, heights[stack.pop()] * (len(heights)-stack[-1]-1))
        return maxArea
