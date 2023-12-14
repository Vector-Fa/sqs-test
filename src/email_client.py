import time

import boto3

from settings import settings

sqs = boto3.client(
    'sqs',
    aws_access_key_id=settings.sqs_access,
    aws_secret_access_key=settings.sqs_secret,
)
queue_url = 'https://sqs.eu-west-1.amazonaws.com/612190425465/Mock_EmailSender'


def send_email(args):
    pass
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=(
            'Information about current NY Times fiction bestseller for '
            'week of 12/11/2016.'
        )
    )

    print(response)
