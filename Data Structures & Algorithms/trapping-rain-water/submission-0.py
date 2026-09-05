class Solution:
    def trap(self, height: List[int]) -> int:
        l_wall, r_wall = 0, 0

        n = len(height)
        area = 0

        max_l, max_r = [0] * n, [0] * n

        for idx, l_h in enumerate(height):
            max_l[idx] = l_wall
            l_wall = max(l_wall, l_h)

            max_r[-idx-1] = r_wall
            r_wall = max(r_wall, height[-idx-1])
        
        for idx in range(n):
            cur = min(max_l[idx], max_r[idx]) - height[idx]

            if cur > 0:
                area += cur
        
        return area