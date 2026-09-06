class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes)
        teams = votes[0]
        k = len(teams)

        count = {}

        for team in teams:
            count[team] = [0] * k

        for vote in votes:
            for i in range(k):
                team = vote[i]
                count[team][i] += 1

        teams = list(teams)
        teams.sort(key=lambda team: ([-x for x in count[team]], team))

        return "".join(teams)