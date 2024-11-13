class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        min_heap = []
        result = []
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        while k>0:
            k-=1
            sum_,i,j=heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])

            if j+1<len(nums2):
                heapq.heappush(min_heap, (nums1[i]+nums2[j+1], i,j+1))
        return result
        

        
    #done

# nums1 = [1,1,2]
nums1= [1,2,4,5,6]
# nums2 = [1,2,3]
nums2 = [3,5,7,9]
k = 3
s = Solution()
s.kSmallestPairs(nums1, nums2, k)
        