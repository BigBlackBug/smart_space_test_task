from celery import Celery
from kombu import Exchange
from kombu import Queue

from multiplier.celery_tasks import MultiplierTask, CombinerTask

BACKEND = "redis://"
BROKER_URL = "amqp://"
CELERY_APP_NAME = "celery"
DEFAULT_QUEUE = "multiplier_queue"

app = Celery(CELERY_APP_NAME, broker=BROKER_URL, backend=BACKEND)
app.conf.task_queues = (
    Queue(DEFAULT_QUEUE, Exchange(DEFAULT_QUEUE), routing_key=DEFAULT_QUEUE),
)
app.conf.task_default_queue = DEFAULT_QUEUE
app.conf.task_default_exchange_type = DEFAULT_QUEUE
app.conf.task_default_routing_key = DEFAULT_QUEUE

app.tasks.register(MultiplierTask)
app.tasks.register(CombinerTask)

app.conf.update(
    task_track_started=True
)
if __name__ == '__main__':
    app.start()
