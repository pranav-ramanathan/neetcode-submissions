class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}

        for idx, num in enumerate(nums):
            complement = target - num

            if complement in check:
                return [check[complement], idx]
            
            check[num] = idx
        
        return [-1, -1]
        