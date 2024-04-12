class Solution:

    dic = {}
    dic[")"] = "("
    dic["]"] = "["
    dic["}"] = "{"

    def isValid(self, s: str) -> bool:
        ls= len(s)
        if ls%2!=0:
            return False

        lst= []

        for i in range(0, ls):
            if not s[i] in self.dic:
                lst.append(s[i])
            else:
                if len(lst)==0:
                    return False
                if self.dic.get(s[i])!=lst.pop():
                    return False
        if len(lst)!=0:
            return False
        return True
            




sol = Solution()
s = "))"

print(sol.isValid(s))



