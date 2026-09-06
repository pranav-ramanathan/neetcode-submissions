class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        pre = 1
        for idx, num in enumerate(nums):
            res[idx] = pre
            pre *= num

        post = 1

        for idx in range(n-1, -1, -1):
            res[idx] *= post
            post *= nums[idx]
        

        
        return res