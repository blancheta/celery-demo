import os

from celery_demo.tasks import other_task

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_demo.settings")
import django
django.setup()

task_count = 100

i = 0

while i < task_count:
    print("Send task to the queue")
    other_task.apply_async(
        args=[],
        queue='feed_tasks',
    )
    i += 1
