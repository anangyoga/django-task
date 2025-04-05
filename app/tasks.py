# calling methods for task-queue
from .methods import do_something
from huey.contrib.djhuey import task

# it means that this function run on the background
@task()
def task_do_something():
    do_something()
