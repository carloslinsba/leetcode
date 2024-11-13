from collections import defaultdict


class Solution:

    def uniqueOccurrences(self, arr: list[int]) -> bool:
        d = defaultdict(0)
        for item in arr:
            d[item]+=1
        l = d.values()
        s = set(l)
        return len(l) == len(s)

            

        

#done