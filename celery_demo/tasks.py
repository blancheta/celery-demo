from time import sleep

from celery_demo.celery import app


@app.task(bind=True, name="Debug task")
def debug_task(self):
     print("booooom!!!")
     sleep(30)
     return "Hello"


@app.task(bind=True, name="Other task")
def other_task(self):
     print("booooom!!!")
     sleep(30)
     return "Hello"