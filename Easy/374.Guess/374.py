# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        maxi = n
        mini=1
        current_guess = mini + (maxi - mini)//2
        result = guess(current_guess)
        
        while result !=0:
            if result <0:
                maxi = current_guess - 1
            else:
                mini = current_guess + 1
            current_guess = mini + (maxi - mini)//2
            result = guess(current_guess)
            
        return int(current_guess)
    

    


#done