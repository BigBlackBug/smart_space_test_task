import random

from celery import chord

from celery_config.celery_init import app
from multiplier.celery_tasks import MultiplierTask, CombinerTask


def _get_random_string():
    return str(random.randint(1, 1000))


def multiply(first, second):
    """
    starts a parallel multiplication job
    :param first: first matrix
    :param second: second matrix
    :return: id of the job
    """
    header = [MultiplierTask().s(i, first[i], second)
              for i in range(len(first))]
    chord_task = chord(header)(CombinerTask().s())
    return chord_task.id


def job_status(job_id: str):
    """
    returns the status of the job
    :param job_id:
    :return: status of the job
    """
    result = app.AsyncResult(job_id)
    return result.state


def get_result(job_id: str):
    """
    returns status of the job and the result matrix if the computation succeeded
    :param job_id:
    :return: tuple status->"", result->[[],[]..]
    """
    async_result = app.AsyncResult(job_id)
    result = None
    if async_result.state == 'SUCCESS':
        result = async_result.get()
    return async_result.status, result
