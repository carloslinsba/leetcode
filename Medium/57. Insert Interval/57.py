class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        i=0
        change = False
        while intervals[i][0] <=newInterval[0]:
            i+=1

        if i>0 and intervals[i-1][1] >= newInterval[0] :
            newInterval = self.merge(newInterval,intervals[i-1]) 
            intervals.pop(i-1)
            intervals.insert(i-1, newInterval)
            change = True
        if newInterval[1] >= intervals[i][0]:
            newInterval = self.merge(intervals[i],newInterval)
            intervals.pop(i)
            intervals.insert(i, newInterval)
            if change:
                intervals.pop(i-1)
            return intervals
        if not (( i>0 and intervals[i-1][1] >= newInterval[0]) or newInterval[1] >= intervals[i][0]) :
            intervals.insert(i, newInterval)
        return intervals

    def merge(self,first:list[int],second:list[int])-> list[int]:
        i= first[0] if first[0] <=second[0] else second[0]
        j = first[1] if first[1] >=second[1] else second[1]
        return [i,j]
        
        

s = Solution()
intervals =[[1,3],[6,9]]
newInterval = [4,6]
print (s.insert(intervals, newInterval))


        #if newInterval[0] > intervals[i-1[1]] 
        #if newInterval[1] < interval[i[0]]
        #then insert

        #if newInterval[0] <= intervals[i-1[1]] then merge
        #if newInterval[1] >= interval[i[0]] then merge

        