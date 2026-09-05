class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights or len(heights) < 2:
            return 0
        
        n = len(heights)
        maxArea = 0

        l, r = 0, n - 1

        while l < r:
            width = r - l

            if heights[l] <= heights[r]:
                maxArea = max(maxArea, width * heights[l])
                l += 1
            else:
                maxArea = max(maxArea, width * heights[r])
                r -= 1
        return maxArea