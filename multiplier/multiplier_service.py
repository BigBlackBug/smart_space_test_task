from celery import chord

from celery_config.celery_init import app
from log_utils import LogFactory
from multiplier.celery_tasks import MultiplierTask, CombinerTask

log = LogFactory.make_log(__name__)


def multiply(first, second):
    """
    starts a parallel multiplication job
    :param first: first matrix
    :param second: second matrix
    :return: id of the job
    """
    tasks = [MultiplierTask().s(i, first[i], second)
             for i in range(len(first))]
    combiner = chord(tasks)(CombinerTask().s())
    log.debug("Multiplier task batch has started")
    return combiner.id


def job_status(job_id: str):
    """
    returns the status of the job
    :param job_id:
    :return: status of the job
    """
    status = app.AsyncResult(job_id).state
    log.debug("Job status for id {} is {}".format(job_id, status))
    return status


def get_result(job_id: str):
    """
    returns status of the job and the result matrix if the computation succeeded
    :param job_id:
    :return: tuple (status->"", result->[[],[]..])
    """
    async_result = app.AsyncResult(job_id)
    result = None
    if async_result.state == 'SUCCESS':
        log.debug("Job status for id {} is {}. Returning result"
                  .format(job_id, async_result.state))
        result = async_result.get()
    else:
        log.debug("Job result for id {} is not ready".format(job_id))
    return async_result.status, result
