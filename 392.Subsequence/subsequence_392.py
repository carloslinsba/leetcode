class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = list(t)
        for letter in s:
            if not (letter in t):
                return False
            t= t[t.index(letter)+1:]
        return True