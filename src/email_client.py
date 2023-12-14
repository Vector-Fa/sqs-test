import time

import boto3
from aiobotocore.session import get_session

from settings import settings

sqs = boto3.client(
    'sqs',
    aws_access_key_id=settings.sqs_access,
    aws_secret_access_key=settings.sqs_secret,
)
queue_url = 'https://sqs.eu-west-1.amazonaws.com/612190425465/Mock_EmailSender'

session = get_session()  # for aioboto3


def send_email(args):
    time.sleep(2)
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=(
            'Information about current NY Times fiction bestseller for '
            'week of 12/11/2016.'
        )
    )

    print(response)


async def send_email_aio(args):
    async with session.create_client(
            'sqs', region_name='eu-west-1',
            aws_access_key_id=settings.sqs_access,
            aws_secret_access_key=settings.sqs_secret) as client:
        response = await client.send_message(QueueUrl=queue_url, MessageBody='test')
        print(response)
