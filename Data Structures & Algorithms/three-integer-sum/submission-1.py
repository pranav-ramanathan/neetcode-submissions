class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        nums.sort()
        n = len(nums)
     
        
        res = []
        
        for idx in range(n):
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            
            if nums[idx] > 0:
                break
            
            start = nums[idx]
            target = -start

            l, r = idx + 1, n - 1
            while l < r:
                cur = nums[l] + nums[r]
                if cur < target:
                    l += 1
                elif cur > target:
                    r -= 1
                else:
                    res.append([start, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

        return res

