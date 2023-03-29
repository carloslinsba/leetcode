class Solution:
    d=dict()
    
    def longestPalindromeHelper(self,s):
        pass

    def longestPalindrome(self, s: str) -> int:
        
        for index, letter in enumerate(s):
            self.d[index] = letter
        



        print(self.d)


a = Solution()
s = "abccccdd"
a.longestPalindrome(s)