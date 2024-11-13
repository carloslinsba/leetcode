class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # s= ""
        # for char in digits:
        #     s+=str(char)
        s = "".join(str(char) for char in digits)
        n = int(s)
        n+=1
        r = str(n)
        l = []
        for char in r:
            l.append(int(char))
        return l

        


        