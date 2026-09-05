from heapq import heappush, heappop
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []

        for num, count in counts.items():
            heappush(heap, (count, num))

            if len(heap) > k:
                heappop(heap)
        
        return [num for _, num in heap]