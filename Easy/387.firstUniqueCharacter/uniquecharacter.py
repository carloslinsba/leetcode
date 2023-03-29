class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=dict()
        for item in s:
            if d.get(item):
                d[item] += 1
            else:
                d[item]=1
        for item in d:
            if d[item]==1:
                return s.index(item)
        return -1
