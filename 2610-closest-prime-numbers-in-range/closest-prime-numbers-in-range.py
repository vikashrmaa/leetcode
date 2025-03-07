class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
    
        def sieve(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False  
            
            for i in range(2, int(math.sqrt(n)) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            
            return is_prime

        prime_flags = sieve(right)

        primes = [i for i in range(left, right + 1) if prime_flags[i]]

        if len(primes) < 2:
            return [-1, -1]

        min_diff = float('inf')
        result = [-1, -1]
        
        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                result = [primes[i], primes[i + 1]]

        return result
