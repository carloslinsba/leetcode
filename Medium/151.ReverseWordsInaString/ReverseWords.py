class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s= s[::-1]
        ret = ""
        return " ".join(s)
        for word in s:
            ret+= word + " "
        return ret[:len(ret)-1:]


st = "the sky is blue"
s =Solution()
print (s.reverseWords(st))