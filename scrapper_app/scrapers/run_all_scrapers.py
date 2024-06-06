from .kupfer4 import run_kupfer_scraper
from .sodimac2 import run_sodimac_scraper
from .servimetal2 import run_servimetal_scraper
from .easy3 import run_easy_scraper
from .constructor31 import run_constructor_scraper
from .construmart2 import run_construmart_scraper
from asgiref.sync import async_to_sync

def run_all_scrapers(channel_layer):
    async_to_sync(channel_layer.group_send)(
        "scrappers", 
        {
            "type": "scrapper.message",
            "message": "Running Kupfer scraper..."
        }
    )
    run_kupfer_scraper()
    
    async_to_sync(channel_layer.group_send)(
        "scrappers", 
        {
            "type": "scrapper.message",
            "message": "Running Sodimac scraper..."
        }
    )
    run_sodimac_scraper()
    
    async_to_sync(channel_layer.group_send)(
        "scrappers", 
        {
            "type": "scrapper.message",
            "message": "Running Servimetal scraper..."
        }
    )
    run_servimetal_scraper()
    
    async_to_sync(channel_layer.group_send)(
        "scrappers", 
        {
            "type": "scrapper.message",
            "message": "Running Easy scraper..."
        }
    )
    run_easy_scraper()
    
    async_to_sync(channel_layer.group_send)(
        "scrappers", 
        {
            "type": "scrapper.message",
            "message": "Running Constructor scraper..."
        }
    )
    run_constructor_scraper()
    
    async_to_sync(channel_layer.group_send)(
        "scrappers", 
        {
            "type": "scrapper.message",
            "message": "Running Construmart scraper..."
        }
    )
    run_construmart_scraper()
