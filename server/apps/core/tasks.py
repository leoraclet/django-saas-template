import random
import time

from celery import shared_task
from faker import Faker
from loguru import logger

from .models import Book


# A pointless Celery task to demonstrate usage
@shared_task
def sample_task():
    logger.info("The sample task just ran.")


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
    retry_backoff=5,
    retry_jitter=True,
    retry_kwargs={"max_retries": 5},
)
def create_book(self, **kwargs):
    if not random.choice([0, 1]):
        # mimic random error
        raise Exception()

    faker = Faker()
    Faker.seed(int(time.time()))
    """
    A Celery task to create a book instance.
    """
    time.sleep(15)  # Simulate a long-running task
    Book.objects.create(
        title=faker.sentence(nb_words=3),
        author=faker.name(),
        content=faker.text(max_nb_chars=200),
        pub_date=faker.date_time_this_decade(),
    )

    logger.info("Book created successfully.")
