from typing import Optional
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        def twoSum(idx: int, target: int):
            l, r = idx + 1, n - 1
            res = []

            while l < r:
                cur = nums[l] + nums[r]

                if cur < target:
                    l += 1
                elif cur > target:
                    r -= 1
                else:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
            return res
        
        for idx in range(n-2):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            
            target = -nums[idx]

            cur = twoSum(idx, target)

            if cur:
                for item in cur:
                    res.append([nums[idx], item[0], item[1]])
        return res