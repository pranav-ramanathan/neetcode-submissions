class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre, post = [1] * (n+1), [1] * (n+1)

        for idx, num in enumerate(nums):
            pre[idx + 1] = pre[idx] * num
        
        for idx, num in enumerate(reversed(nums)):
            post[n - 1 - idx] = post[n - idx] * num
        
        res = [1] * n

        for idx in range(n):
            res[idx] = pre[idx] * post[idx + 1]
        
        return res
