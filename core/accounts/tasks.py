from celery import shared_task
from time import sleep
from core.celery import Celery


@shared_task
def send_email_task():
    sleep(3)
    print("Done Sending Email")

# or

# @Celery.task
# def send_email():
#     sleep(3)
#     print("Done Sending Email")
