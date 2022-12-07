import os

from celery import Celery


celery = Celery("tasks")
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0")
celery.autodiscover_tasks(["worker"])
celery.conf.result_backend_transport_options = {
    'retry_policy': {
        'timeout': 5.0
    }
}
