import unittest

from celery import chord

from celery_config.celery_init import app
# s is a signature
from multiplier.celery_tasks import MultiplierTask, CombinerTask


class TestMyCeleryWorker(unittest.TestCase):
    def setUp(self):
        app.conf.update(CELERY_ALWAYS_EAGER=True)

    def test_worker(self):
        """
        Testing that multiplication works as expected
        :return:
        """
        first = [[4, 2, 1], [5, 3, 6], [0, 7, 8]]
        second = [[9, -4], [-1, 2], [0, -2]]

        header = [MultiplierTask().s(i, first[i], second)
                  for i in range(len(first))]
        chord_task = chord(header)(CombinerTask().s())
        expected = [[34, -14], [42, -26], [-7, -2]]
        self.assertEqual(expected, chord_task.get())
