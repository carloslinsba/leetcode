class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        for j in range(0, len(haystack)):
            i=0
            for index in range(j, len(haystack)):
                item = haystack[index]
                if item==needle[i]:
                    i+=1
                    if i==len(needle):
                        return index - (i -1)
                else:
                    i=0
                    break

        return -1



s= Solution()
haystack = "aabaabbbaabbbbabaaab"
needle = "abaa"
print (s.strStr(haystack, needle))