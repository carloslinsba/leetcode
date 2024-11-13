class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = {}
        for item in nums:
            if d.get(item):
                d[item]+=1
            else: 
                d[item]=1
        heap=[]
        for key,value in d.items():
            heapq.heappush(heap, (-value, key))
        
        result = []
        for i in range(k):
            _, key = heapq.heappop(heap)
            result.append(key)
        
        return result



#done