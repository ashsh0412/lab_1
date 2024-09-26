def is_prime(n):
    if n == 2:
        return True
    elif n <=1:
        return False
    else:
        for i in range(2,n):
            if n%i == 0:
                return False
            return True
    
def prime_factors_sqrt(n):
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    if n > 2:
        factors.append(n)
    
    return factors

def prime_factors_full(n):
    factors = []
    
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    return factors

def prime_factors_recursive(n, i=2):
    if n == 1:
        return []
    if i > n:
        return [n]
    if n % i == 0:
        return [i] + prime_factors_recursive(n // i, i)
    return prime_factors_recursive(n, i + 1)
    
def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    p = 2
    while (p ** 2 <= limit):
        if primes[p]:
            for i in range(p ** 2, limit + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, limit + 1) if primes[p]]

def prime_factors_sieve(n):
    factors = []
    primes = sieve_of_eratosthenes(n)
    
    for prime in primes:
        while n % prime == 0:
            factors.append(prime)
            n //= prime
    
    return factors
