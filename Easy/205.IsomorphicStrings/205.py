class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        dic_t = {}
        
        for i in range(0, len(s)):
            if not s[i] in dic:
                dic[s[i]]= t[i]
                if t[i] in dic_t:
                    return False
                dic_t[t[i]]=s[i]
                continue
            if t[i]!=dic[s[i]]:
                return False
        return True
        


s = "paper" 
t = "title"
sol = Solution()
print(sol.isIsomorphic(s,t))