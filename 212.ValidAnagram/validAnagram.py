class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        dic = dict()
        for item in s:
            if dic.get(item):
                dic[item]+=1
            else:
                dic[item]=1
        for item in t:
            if not dic.get(item):
                return False
            else:
                dic[item]-=1
                if dic[item]==0:
                    dic.pop(item)
        return True

