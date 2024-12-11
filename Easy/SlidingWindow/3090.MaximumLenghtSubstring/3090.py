from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        d = defaultdict(int)
        left =0
        right=0
        max_len=1
        c_len=1
        d[s[left]]+=1

        while right<len(s):            
            if left ==right:
                right+=1
                d[s[right]]+=1
                c_len+=1
                continue
            if d[s[right]]>2:
                d[s[left]]-=1
                left+=1
                c_len-=1
                if c_len>max_len:
                    max_len=c_len
                continue
            if right+1>=len(s):
                break
            right+=1
            d[s[right]]+=1
            c_len+=1
        if c_len> max_len:
            max_len=c_len
        return max_len
            

#n= "acedc" 
n="bcbbbcba"
print( Solution().maximumLengthSubstring(n))           

#time complexity: O(n)
#space complexity:O(n)