class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        sequences = set()
        res = set()
        for i in range(10,len(s)+1):
            seq = s[i-10:i]
            if seq in sequences:
                res.add(seq)
            else:
                sequences.add(seq)
        return list(res)

#time complexity: O(n)
#space complexity: O(n)


s ="AAAAAAAAAAA"

print(Solution().findRepeatedDnaSequences(s))