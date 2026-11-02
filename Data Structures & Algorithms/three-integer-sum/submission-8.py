class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for idx in range(n-2):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            
            if nums[idx] > 0:
                break

            target = -nums[idx]

            l, r = idx+1, n-1

            while l < r:
                cur = nums[l] + nums[r]

                if cur == target:
                    res.append([nums[idx], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                
                elif cur < target:
                    l += 1
                else:
                    r -= 1
            
        return res


