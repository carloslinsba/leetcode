class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        def isGood(s:str):
            return True if s[0]!=s[1] and s[0]!=s[2] and s[1]!=s[2] else False
            # return True if len(set(s))==3 else False


        results= 0
        for i in range(len(s)):
            if i+3>len(s):
                break
            s2 =s[i:i+3]
            if isGood(s2):
                results+=1
        return results


#time complexity: O(n)
#space complexity: O(n)


#done
