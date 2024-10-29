def fibonacci(n):
    fib_sequence = [0, 1]

    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return fib_sequence[n - 1]


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(1, n + 1):
        if n % i == 0 and i != 1 and i != n:
            return False

    return True


def print_prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    if n > 2:
        factors.append(n)

    print(eval(" * ".join(map(str, factors))), "=", " * ".join(map(str, factors)))
