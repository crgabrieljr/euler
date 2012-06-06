"""
This seems like a graph path finding problem on it's face,
but is really a combinatorics problem.

Think of it as the number of ways we can arrange a list of
moves of the form:
right1, right2, right3, ... down1, down2, down3, ...

The solution turns out to be the number of permutations
of that list with the duplications factored out.

For a square grid, this is conveniently 2*n choose n where
n is the size of the grid or 2*n! / (n!)^2

For a non-square grid, it is (width+height)! / width! / height! or
(width+height)! / (width! * height!)
"""

from math import factorial

print factorial(40) / factorial(20)**2

"""
from euler import lib
from numpy import matrix


def square_matrix(size):
    return [[0 for x in range(size)] for x in range(size)]


def square_mesh_network(size):
    adj = square_matrix(size**2)
    for i in range(size**2):
        row = i / size
        col = i % size
        top = i - size
        left = i - 1
        right = i + 1
        bottom = i + size
        if col > 0:
            adj[i][left] = 1
        if col < size - 1:
            adj[i][right] = 1
        if row > 0:
            adj[i][top] = 1
        if row < size - 1:
            adj[i][bottom] = 1

    return adj


adj = matrix(square_mesh_network(21))

path_matrix = adj**40

print path_matrix[0, -1]
"""

