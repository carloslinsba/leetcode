class Solution:
    def lengthOfLongestSubstringHelper(self, s: str) -> int:
        d = dict()
        for index, item in enumerate(s):
            if d.get(item):
                return index
            d[item]=1
        return len(s)

    def lengthOfLongestSubstring(self, s: str) -> int:
        biggestLength=0
        s_index=0
        while s_index<len(s):
            if biggestLength > len(s)-s_index:
                return biggestLength
            currentLength = self.lengthOfLongestSubstringHelper(s[s_index:])
            s_index+=1
            if currentLength> biggestLength:
                biggestLength=currentLength
        return biggestLength