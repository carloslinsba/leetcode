
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
                
        left=0
        right =k
        
        count=0
        for j in range(left,right):
                count+= 1 if (blocks[j]=="W") else 0
        min_count = count

        while right<len(blocks):
            left+=1
            right+=1
            count-=1 if (blocks[left-1])=="W" else 0
            count+=1 if (blocks[right-1])=="W" else 0
            if count<min_count:
                min_count=count
            
        return min_count
            
#time complexity: O(n*logn) 
#space complexity: O(1)

            
