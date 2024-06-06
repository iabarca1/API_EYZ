# scraper_app/scrapers/run_all_scrapers.py

from .kupfer4 import run_kupfer_scraper
from .sodimac2 import run_sodimac_scraper
from .servimetal2 import run_servimetal_scraper
from .easy3 import run_easy_scraper
from .constructor31 import run_constructor_scraper
from .construmart2 import run_construmart_scraper

def run_all_scrapers():
    run_kupfer_scraper()
    run_sodimac_scraper()
    run_servimetal_scraper()
    run_easy_scraper()
    run_constructor_scraper()
    run_construmart_scraper()
