class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        cited=0
        count=0
        for i in range(len(citations)-1,-1,-1):
            cited = citations[i]
            if cited>count:
                count+=1
            else:
                break
        return count


s = Solution()
#citations = [3,0,6,1,5]
citations = [1,3,1,1,2]
print(s.hIndex(citations))