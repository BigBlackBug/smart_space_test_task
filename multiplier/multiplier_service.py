import random


def _get_random_string():
    return str(random.randint(1, 1000))


def multiply(first, second):
    """
    starts a parallel multiplication job
    :param first: first matrix
    :param second: second matrix
    :return: id of the job
    """
    # TODO implement
    return _get_random_string()


def job_status(job_id: str):
    """
    returns the status of the job
    :param job_id:
    :return: status of the job
    """
    return _get_random_string()


def get_result(job_id: str):
    """
    returns status of the job and the result matrix if the computation succeeded
    :param job_id:
    :return: tuple status->"", result->[[],[]..]
    """
    return _get_random_string(), [[]]
