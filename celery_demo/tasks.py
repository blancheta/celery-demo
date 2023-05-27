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


@app.task(bind=True)
def scheduled_task(self, arg):
    return arg

# @app.task(bind=True)
# def scheduled_task_with_param(arg):
#     return arg
#
# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(10.0, scheduled_task_with_param.s('hello'), name='add every 10')
