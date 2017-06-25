from celery import Task

from multiplier.matrix import Matrix


class MultiplierTask(Task):
    name = 'multiplier'

    def run(self, i, horizontal_vector, second_matrix):
        """
        multiplies a vector by a matrix
        :param i: index of a vector in the first matrix
        :param horizontal_vector:
        :param second_matrix:
        :return: tuple (i:int, row) where row is a product of multiplication
        """
        height = len(second_matrix)
        width = len(second_matrix[0])
        row = [0] * width
        for j in range(0, width):
            for k in range(0, height):
                row[j] += horizontal_vector[k] * second_matrix[k][j]
        return i, row


class CombinerTask(Task):
    name = 'matrix_combiner'

    def run(self, results, *args, **kwargs):
        """
        :param results: list of tuples (i:int, row:list)
        :param args:
        :param kwargs:
        :return:
        """
        # length of the first row
        width = len(results[0][1])
        matrix = Matrix.make_matrix(width, len(results), lambda: 0)
        # building the matrix row by row
        for i, row in results:
            matrix[i] = row
        return matrix.values
