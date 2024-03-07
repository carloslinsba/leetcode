class Solution:

    def candy(self, ratings: list[int]) -> int:
        sorted_ratings = ratings.copy().sort()
        for rat in sorted_ratings:
            idx= ratings.index(rat)
            if ratings[idx-1]<rating[idx] or ratings[idx +1]<rating[idx]:
                

            
        

#sort the array
# go from smallest rating to biggest rating:
#   loop:
#   does it has a neighboor with a smaller rating ?
#   if so: they receive: (biggest smaller) neighboor+1
#   if not: receive 01
#do it until finish it


        

s = Solution()
#ratings = [1,0,2]
ratings = [1,2,2]

print(s.candy(ratings))