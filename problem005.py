from sys import argv

from euler.lib import gcd, lcm


n = int(argv[1])
product = 2
for x in xrange(3, n + 1):
    product = lcm(product, x)

print product

