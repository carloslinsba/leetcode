class Solution:
    
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        isoDict = {

        }
        for idx,letter in enumerate(s):
            if isoDict.get(letter):
                 if isoDict.get(letter)!= t[idx]:
                    return False
            else:
                if t[idx] in isoDict.values():
                    return False
                isoDict[letter] = t[idx]
        return True

st = "paper" 
t = "title"
s = Solution()
print( s.isIsomorphic(st, t) )
