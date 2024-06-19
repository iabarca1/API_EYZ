from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .scrapers.kupfer4 import run_kupfer_scraper

@shared_task
def run_kupfer_scraper_task():
    channel_layer = get_channel_layer()
    
    async_to_sync(channel_layer.group_send)(
        "scrappers", 
        {
            "type": "scrapper.message",
            "message": "Starting Kupfer scraper..."
        }
    )
    
    result = run_kupfer_scraper()
    
    async_to_sync(channel_layer.group_send)(
        "scrappers", 
        {
            "type": "scrapper.message",
            "message": "Kupfer scraper finished successfully",
            "data": result
        }
    )
    
    return result
