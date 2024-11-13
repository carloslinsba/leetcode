class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        if len(score)==1:
            return ["Gold Medal"]

        score_copy = score.copy()
        score_copy.sort(reverse=True)
        answer = []
        for idx, athlete_scores in enumerate(score):
            answer.append(str(score_copy.index(athlete_scores)+1))
        answer[answer.index("1")]= "Gold Medal"
        answer[answer.index("2")]= "Silver Medal"
        if len(score)>=3:
            answer[answer.index("3")]= "Bronze Medal"
        return answer
        

#done