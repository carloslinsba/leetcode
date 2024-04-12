class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic ={}
        for letter in magazine:
            if dic.get(letter):
                dic[letter]+=1
            else:
                dic[letter]= 1
        for letter in ransomNote:
            if not dic.get(letter):
                return False
            dic[letter]-=1
            if dic[letter]<0:
                return False
        return True



ransomNote = "aa"
magazine = "aab"
sol = Solution()
print(sol.canConstruct(ransomNote, magazine))
        
