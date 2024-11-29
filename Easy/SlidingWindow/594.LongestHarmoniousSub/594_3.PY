from collections import defaultdict


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        d = defaultdict(int)
        long=0
        for number in nums:
            d[number] += 1
        for n in d.keys():
            if n+1 in d:
                long =max(long, d[n] + d[n+1])
        return long


