class Solution:
    response = []
    def printSequence(self, start, end):
        s = str(start)
        if not end is None:
            s=s+"->"+str(end)
        self.response.append(s)
        return


    def summaryRanges(self, nums: list[int]) -> list[str]:
        self.response = []
        previous_num=None
        start_seq=None
        last_seq=None
        i=0
        for i, num in enumerate(nums):
            if previous_num is None:
                previous_num=num
                continue
            if num-previous_num==1:
                if start_seq is None:
                    start_seq=previous_num
                last_seq=num
            else:
                if start_seq is None:
                    start_seq= previous_num
                self.printSequence(start_seq, last_seq)
                start_seq=None
                last_seq=None
            previous_num=num

        if i==len(nums)-1:
            if start_seq is None:
                start_seq=previous_num
            self.printSequence(start_seq, last_seq)
        return self.response


s= Solution()
#nums = [0,1,2,4,5,7]
#nums = [0,2,3,4,6,8,9]
nums = []
print (s.summaryRanges(nums))
                
