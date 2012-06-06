from sys import stdout


lengths = {1: 1}

def get_sequence_len(n):
    if n in lengths:
        return lengths[n]
    elif n & 1:
        seq_len = 1 + get_sequence_len(3 * n + 1)
    else:
        seq_len = 1 + get_sequence_len(n / 2)
    lengths[n] = seq_len
    return seq_len

start_max = 0
max_length = 0
for n in xrange(1000000, 0, -1):
    stdout.write('\rtesting %d' % n)
    stdout.flush()
    seq_len = get_sequence_len(n)
    if seq_len > max_length:
        start_max = n
        max_length = seq_len

print '\n\n%d resulted in the longest sequence' % start_max

