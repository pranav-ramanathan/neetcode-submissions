class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre = [1] * (n+1)

        for idx, num in enumerate(nums):
            pre[idx+1] *= pre[idx] * num
        
        post = [1] * (n+1)

        for idx in range(n, 0, -1):
            post[idx - 1] = post[idx] * nums[idx-1]
        
        res = [1] * n

        for idx in range(n):
            res[idx] = pre[idx] * post[idx + 1]
        
        return res