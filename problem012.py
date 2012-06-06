from sys import argv

from euler.lib import sieve


primes = list(sieve(1000))

factor_counts = {}
def num_factors(num):
    count = factor_counts.get(num)
    if not count:
        count = 1
        for prime in primes:
            if prime**2 > num:
                count *= 2
                break
            exp = 1
            while not num % prime:
                exp += 1
                num /= prime
            count *= exp
            if num == 1:
                break

    factor_counts[num] = count
    return count


if __name__ == '__main__':
    n = 2
    while True:
        tn = n * (n + 1) / 2
        nf = num_factors(n)
        if n & 1:
            nf *= num_factors((n + 1) / 2)
        else:
            nf * num_factors(n + 1)
        if nf >= int(argv[1]):
            break
        n += 1

    print '%s: %s: %s' % (n, tn, nf)

