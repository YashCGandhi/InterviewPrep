# Sieve of Eratosthenes Algo on wikipedia
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [False, False] + [True] * (n - 2)
        for i in range(2,int(sqrt(n)) + 1):
            if primes[i]:
                j = i*i
                while j <= n - 1:
                    primes[j] = False
                    j += i
                
        return sum(primes)
