class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s=str(num)
        result=0
        for i in range(len(s)):
            if i+k>len(s):
                break
            cur = int(s[i:i+k])
            if cur!=0 and num%cur==0:
                result+=1
        
        return result


#time complexity: O(n)
#space complexity: O(n)