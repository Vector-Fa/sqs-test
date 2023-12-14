from fastapi import APIRouter, BackgroundTasks

from celery_app import celery_app, queue_name
from email_client import send_email, send_email_aio

router = APIRouter()


@router.post('/email/raw')
async def send_email_raw(background_task: BackgroundTasks):
    send_email(
        ('email', 12)
    )
    return {'message': 'done'}


@router.post('/email/backgroundTask')
async def send_email_task(background_task: BackgroundTasks):
    background_task.add_task(send_email, ('email', 12))
    return {'message': 'done'}


@router.post('/email/aioboto')
async def send_email_aioboto():
    await send_email_aio('test')
    return {'message': 'done'}


@router.post('/email/celery')
async def send_email_celery():
    celery_app.send_task(queue_name, args=(1, 2, 3,))
    # celery_app.signature(queue_name, args=(1, 2, 3,)).apply_async()
    return {'message': 'done'}


@router.get('/test')
async def test():
    return {'message': True}