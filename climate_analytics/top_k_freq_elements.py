import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return
        
        nums_dict = {}

        k_heap = []

        for item in nums:
            nums_dict[item] = nums_dict.get(item, 0) + 1
        
        for item, freq in nums_dict.items():
            print(k_heap)
            if len(k_heap) < k:
                heapq.heappush(k_heap, (freq, item))
            elif freq > k_heap[0][0]:
                heapq.heapreplace(k_heap, (freq, item))
        
        print(k_heap)
        result = [x for _, x in k_heap]

        return result
