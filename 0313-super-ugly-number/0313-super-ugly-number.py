class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        ugly = [0] * n
        ugly[0] = 1
        index = [0] * k

        for i in range(1, n):
            next_num = float('inf')

            for j in range(k):
                value = ugly[index[j]] * primes[j]
                if value < next_num:
                    next_num = value

            ugly[i] = next_num

            for j in range(k):
                if ugly[index[j]] * primes[j] == next_num:
                    index[j] += 1

        return ugly[n - 1]