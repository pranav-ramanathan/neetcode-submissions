class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        pre = post = 1

        for idx, num in enumerate(nums):
            res[idx] *= pre
            pre *= num
        
        for idx in range(n-1, -1, -1):
            num = nums[idx]
            res[idx] *= post
            post *= num
        return res
        
