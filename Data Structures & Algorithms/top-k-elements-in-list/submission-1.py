from collections import Counter
from heapq import heappop, heappush
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counts = Counter(nums)

        for num, count in counts.items():
            heappush(heap, (count, num))

            if len(heap) > k:
                heappop(heap)
        
        return [num for _, num in heap]