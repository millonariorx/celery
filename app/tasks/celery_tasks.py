from app.config.celery_config import celery_app
import time

@celery_app.task
def add(x, y):
    time.sleep(5)
    return x + y

@celery_app.task
def multiply(x, y):
    time.sleep(3)
    return x * y

@celery_app.task
def subtract(x, y):
    time.sleep(2)
    return x - y

@celery_app.task
def divide(x, y):
    time.sleep(20)
    return x / y if y != 0 else 'Division by zero error'
