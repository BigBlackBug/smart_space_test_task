import random


def make_matrix(rows, cols,
                generator=lambda: random.randint(1, 10)):
    return [[generator() for i in range(cols)] for j in
            range(rows)]
