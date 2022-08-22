import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pasantic_backend.settings')

app = Celery('pasantic_backend')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.update(
    BROKER_URL = 'redis://127.0.0.1:6379/0',
)

app.conf.beat_schedule = {
    'reboot-cache-main-crontab': {
        'task': 'internships.tasks.reboot_cache_main_crontab',
        'schedule': crontab(minute="*"),
    },
}
