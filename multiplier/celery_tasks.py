from celery import Task
from celery.utils.log import get_task_logger

from multiplier import utils

logger = get_task_logger(__name__)


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
        rows = len(second_matrix)
        cols = len(second_matrix[0])
        row = [0] * cols
        for j in range(0, cols):
            for k in range(0, rows):
                row[j] += horizontal_vector[k] * second_matrix[k][j]
        return [i, row]


class CombinerTask(Task):
    name = 'matrix_combiner'

    def run(self, results):
        """
        :param results: list of tuples (i:int, row:list)
        :param args:
        :param kwargs:
        :return:
        """
        # TODO a huge workaround
        # celery.chord ignores the outer list if the number
        # of rows of the result is 0
        if len(results) == 2:
            if type(results[0]) == int and type(results[1] == list):
                results = [results]
        # length of the first row
        cols = len(results[0][1])
        matrix = utils.make_matrix(len(results), cols)
        # building the matrix row by row
        for i, row in results:
            matrix[i] = row
        return matrix
