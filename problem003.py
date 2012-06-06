from itertools import ifilter
from sys import argv

from euler.lib import gcd, pollard_rho, sieve


def max_prime_factor(num, primes):
    primes = ifilter(lambda x: x <= num / 2, primes)
    for x in primes:
        if not num % x:
            return x
    return num


if __name__ == '__main__':
    n = int(argv[1])
    factors = pollard_rho(n, lambda x: (x**2 + 1) % n)
    if factors:
        primes = list(sieve(max(factors) / 2, ascending=False))
        print max(map(lambda x: max_prime_factor(x, primes), factors))
    
