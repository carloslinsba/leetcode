class Solution:
    def longestPalindrome(self, s: str) -> int:
        word_max_index = len(s) -1
        if word_max_index==0:
            return 1

        palindrome = 1
        for i in range(1,word_max_index):
            previous_letter = s[i-1]
            current_letter = s[i]
            next_letter= s[i+1]
            if not next_letter:
                return palindrome

            if previous_letter == next_letter:
                if palindrome==1:
                    palindrome+=1
                palindrome+=1


        pass


    #carlosa
    #asolrac
    #carlosa
    #salrcsa
#next letter should be equal to previous letter
    