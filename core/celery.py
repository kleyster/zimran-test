from __future__ import absolute_import
import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))

# app.conf.beat_schedule = {
#
#     'print-message-ten-seconds': {
#         # Task Name (Name Specified in Decorator)
#         'task': 'print_msg_main',
#         # Schedule
#         'schedule': 10.0,
#         # Function Arguments
#         'args': ("Hello",)
#     },
# }