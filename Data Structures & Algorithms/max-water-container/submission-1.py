class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        l, r = 0, len(heights) - 1

        while l < r:
            if heights[l] <= heights[r]:
                cur = (r - l) * heights[l]
                l += 1
            else:
                cur = (r - l) * heights[r]
                r -= 1
            
            max_area = max(cur, max_area)

        return max_area
        