from sys import argv


def find_m_and_n(num):
    for m in xrange(num / 2, 0, -1):
        for n in xrange(m - 1, 0, -1):
            if 2 * m**2 + 2 * m * n == num:
                return m, n


if __name__ == '__main__':
    m, n = find_m_and_n(int(argv[1]))
    print (m**2 - n**2) * (2 * m * n) * (m**2 + n**2)
