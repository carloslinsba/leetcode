
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
                
        blocks = ["0" if item =="B" else "1" for item in blocks]
        left=0
        right =k
        
        count=0
        for j in range(left,right):
                count+= int(blocks[j])
        min_count = count

        while right<len(blocks):
            left+=1
            right+=1
            count-=int(blocks[left-1])
            count+=int(blocks[right-1])
            if count<min_count:
                min_count=count
            
        return min_count
            
#time complexity: O(n*logn) 
#space complexity: O(1)

            
