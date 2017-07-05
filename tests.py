import unittest

from multiplier.celery_tasks import MultiplierTask, CombinerTask


class TestMyCeleryWorker(unittest.TestCase):
    def test_worker(self):
        """
        Testing that multiplication works as expected
        :return:
        """
        first = [[4, 2, 1], [5, 3, 6], [0, 7, 8]]
        second = [[9, -4], [-1, 2], [0, -2]]

        header = [MultiplierTask().run(i, first[i], second)
                  for i in range(len(first))]
        result = CombinerTask().run(header)
        expected = [[34, -14], [42, -26], [-7, -2]]
        self.assertEqual(expected, result)

    def test_small_matrix(self):
        """
        Testing that multiplication works as expected
        :return:
        """
        first = [[1]]
        second = [[1], [2], [3]]

        header = [MultiplierTask().run(i, first[i], second)
                  for i in range(len(first))]
        result = CombinerTask().run(header)
        expected = [[1], [2], [3]]
        self.assertEqual(expected, result)
