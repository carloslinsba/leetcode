class Solution:
    # Given a pattern and a string s, find if s follows the same pattern. Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
    #Input: pattern = "abba", s = "dog cat cat dog"
 #Output: true
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s)!= len(pattern):
            return False
        isoDict = {

        }
        for idx,letter in enumerate(pattern):
            if isoDict.get(letter):
                 if isoDict.get(letter)!= s[idx]:
                    return False
            else:
                if s[idx] in isoDict.values():
                    return False
                isoDict[letter] = s[idx]
        return True
        
