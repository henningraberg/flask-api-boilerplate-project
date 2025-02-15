from os import environ
from celery import Celery

# environ.setdefault('CELERY_CONFIG_MODULE', 'celery_config')

# app = Celery()
# app.config_from_envvar('CELERY_CONFIG_MODULE')

CELERY_BROKER_URL = 'amqp://user:password@localhost:5672/'

app = Celery('queue', broker=CELERY_BROKER_URL)


@app.task
def add(x, y):
    return x + y


@app.task
def tsum(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args[0])
