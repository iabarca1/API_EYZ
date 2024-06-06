# scrapper_app/tasks.py

from celery import shared_task
from .scrapers.run_all_scrapers import run_all_scrapers

@shared_task
def run_all_scrapers_task():
    run_all_scrapers()
