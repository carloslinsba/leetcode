class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        for i in range(1, n+1):
            if (i)%3==0:
                answer.append("Fizz")
                if i%5==0:
                    answer[i-1]+=("Buzz")
                    continue
            if (i)%5==0:
                answer.append("Buzz")
            if not (i%3==0 or i%5==0):
                answer.append(str(i))
        return answer

s = Solution()
print (s.fizzBuzz(15) )


