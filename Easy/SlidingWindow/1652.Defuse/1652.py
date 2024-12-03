class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        l=[]
        if k==0:
            return [0 for i in code]
        if k>0:
            count=0
            for j in range(k):
                n= (j+1 - (len(code))) if (j+1>=len(code)) else (j+1)
                count += code[n]
            l.append(count)
            for i in range(1,len(code)):
                count-=code[i]
                count += code[i+k] if i+k<len(code) else code[(i+k)-len(code)]
                l.append(count)
        else:
            count =0
            for j in range(0,k,-1):
                count+= code[j-1]
            l.append(count)
            for i in range(1,len(code)):
                count-=code[k+i-1]
                count+=code[i-1]
                l.append(count)
        return l

#done
#time complexity O(n)
#space complexity O(n)



        