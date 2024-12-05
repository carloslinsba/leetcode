class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        if len(t)==0:
            return False
        
        i=0
        for j in range(len(t)):
            if s[i] == t[j]:
                i+=1
                if i>=len(s):
                    return True
            continue
        if i==len(s):
            return True
        return False

sol= Solution()
s = "axc"
t = "ahbgdc"
print(sol.isSubsequence(s,t))
