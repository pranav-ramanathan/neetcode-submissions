class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        l, r = 0, len(heights) - 1

        while l < r:
            width = r - l
            cur = min(heights[l], heights[r]) * width
            max_area = max(max_area, cur)

            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_area