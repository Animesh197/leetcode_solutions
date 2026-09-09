class Solution:
    def countCommas(self, n: int) -> int:
        answer = 0
        power = 1000

        while power <= n:
            answer += n - power + 1
            power *= 1000

        return answer