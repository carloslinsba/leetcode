class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        #magazine = list(magazine)
        for letter in  ransomNote:
            if letter not in magazine:
                return False
            #magazine.pop(magazine.index(letter))
            magazine = magazine.replace(letter, "",1)
        return True

                
s = Solution()
ransomNote = "aa"
magazine = "aba"
print (s.canConstruct(ransomNote, magazine))


        