class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        count=0
        for idx, letter in enumerate(strs[0]):
            for word in strs[1:]:
                if len(word)<=idx or letter != word[idx] :
                    return strs[0][:count:]
            count+=1
        return strs[0]
                

            


#strs = ["flower","flow","flight"]
strs = ["flower","flow","flight", "fs"]
#strs =["dog","racecar","car"]
#strs= [""]
s = Solution()
print(s.longestCommonPrefix(strs))