import random


class Matrix:
    def __init__(self, height=None, width=None, values=None):
        self.width = width
        self.height = height
        self.values = values

    @staticmethod
    def make_matrix(width, height, generator=lambda: random.randint(1, 10)):
        return Matrix(width, height,
                      [[generator() for i in range(width)] for j in
                       range(height)])

    def __getitem__(self, item):
        return self.values[item]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __eq__(self, other):
        for i in range(len(self.values)):
            if self.values[i] != other[i]:
                return False
        return True
