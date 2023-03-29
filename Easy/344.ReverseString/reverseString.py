class Solution:
    def reverseString(self, s: list[str]) -> None:
        for index in range(0, len(s)-1):
            n = s.pop(len(s)-1)
            s.insert(index, n)
            
            


        """
        Do not return anything, modify s in-place instead.
        """