from celery import Celery

from settings import settings

broker_url = f'sqs://{settings.sqs_access}:{settings.sqs_secret}@'
# broker_url = 'amqp://guest:guest@localhost:5672/'
queue_name = 'Mock_EmailSender'
broker_transport_options = {'region': 'eu-west-1'}

celery_app = Celery(broker_url=broker_url)
celery_app.conf.task_default_queue = queue_name
celery_app.conf.task_create_missing_queues = False
