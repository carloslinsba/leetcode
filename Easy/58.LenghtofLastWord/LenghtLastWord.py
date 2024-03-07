class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strList = s.split()
        return len(strList.pop(len(strList)-1))