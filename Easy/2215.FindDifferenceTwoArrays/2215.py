class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        s1 = set(nums1)
        s2 = set(nums2)

        answer=[[],[]]

        for item in s1:
            if item not in s2:
                answer[0].append(item)
        for item in s2:
            if item not in s1:
                answer[1].append(item)

        return answer



#done