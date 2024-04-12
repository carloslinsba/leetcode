class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        

        s_left=0
        s_right=len(s)-1
        i=0
        j=len(t)-1
        while(s_left<=s_right and i<=j):
            if s[s_left]==t[i]:
                s_left+=1
            if s[s_right]==t[j] and i!=j:
                s_right-=1
            i+=1
            j-=1

        if s_left>s_right:
            return True
        return False
                
sol= Solution()
s = "bb"
t = "abc"
print(sol.isSubsequence(s,t))
                


        
