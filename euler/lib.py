def gcd(a, b):
    if not b:
        return a
    if a < b:
        return gcd(b, a)
    if not a % b:
        return b
    return gcd(b, a % b)


def lcm(a, b):
    if not b % a:
        return b
    if not a % b:
        return a
    return b * (a / gcd(a, b))


def matrix_exponent(matrix, exponent):
    return reduce(matrix_multiply, [matrix] * exponent)


def matrix_multiply(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    if len(B) != n:
        raise ValueError
    result =[[0 for col in range(p)] for row in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
        
    return result


def pollard_rho(n, f=None):
    f = f or (lambda x: (x**2 + 1) % n)
    x = y = 2
    d = 1
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)

    if d == n:
        return [n]
    else:
        return [d] + pollard_rho(n / d, f)


def sieve(limit, ascending=True):
    sqrt_limit = int(limit**.5)
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in xrange(2, sqrt_limit + 1):
        if primes[i]:
            j = i
            while True:
                k = i * j
                if k > limit:
                    break
                primes[k] = False
                j += 1

    if ascending:
        return (x for x in xrange(2, limit + 1) if primes[x])
    else:
        return (x for x in xrange(limit, 1, -1) if primes[x])
