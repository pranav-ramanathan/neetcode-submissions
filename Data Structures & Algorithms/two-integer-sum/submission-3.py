class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for idx, num in enumerate(nums):
            if num in res:
                return [res[num], idx]

            cur = target - num
            res[cur] = idx