# Celery Demo

This project sends two different type of tasks x100.

### Create virtualenv

I installed Python3.10 to run this project.

```
python -m venv venv
```

### Install dependencies

```
source venv/bin/activate
pip install -r requirements.txt
```

### Run the project

To run the celery worker
```
celery -A celery_demo worker -Q feed_tasks -l DEBUG -E
```

To run flower
```
celery --broker=redis://localhost:6379// flower --port=5566
```

To run the feeders
```
python feeder1.py
python feeder2.py
```

Run Celery beat with one task every 10 seconds
[https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html#crontab-schedules](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html#crontab-schedules)
```
celery -A celery_demo beat -l debug
```
