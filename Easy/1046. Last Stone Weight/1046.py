class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []
        for x in stones:
            heapq.heappush(heap, -x )
        
        while len(heap)>1:
            a = - heapq.heappop(heap)
            b = - heapq.heappop(heap)
            new_stone = a-b if a!=b else None
            if new_stone:
                heapq.heappush(heap, -new_stone)
        return - heapq.heappop(heap) if len(heap)>0 else 0
        




        