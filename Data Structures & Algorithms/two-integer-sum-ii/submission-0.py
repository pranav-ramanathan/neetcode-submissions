class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return [-1, -1]
        
        n = len(numbers)
        l, r = 0, n - 1
        while l < r:
            cur = numbers[l] + numbers[r]
            if cur == target:
                return [l+1, r+1]
            elif cur < target:
                l += 1
            else:
                r -= 1
        
        return [-1, -1]
        