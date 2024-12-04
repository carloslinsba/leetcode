#naive approach
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
                
        blocks = ["0" if item =="B" else "1" for item in blocks]
        min_count=k
        for i in range(len(blocks)):
            if i+k>len(blocks):
                break
            count=0
            for j in range(i,i+k):
                count+= int(blocks[j])
            if count<min_count:
                min_count=count
        return min_count
            
#time complexity: O(n*k) -> O(nˆ2)
#space complexity: O(1)

            
