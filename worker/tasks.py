import time

from worker.celery import celery


@celery.task
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True
