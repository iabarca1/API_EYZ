# scrapper_app/urls.py

from django.urls import path
from .views import ScrapedDataList, RunKupferScraperView, RunAllScrapersView

urlpatterns = [
    path('scraped-data/', ScrapedDataList.as_view(), name='scraped-data-list'),
    path('run-kupfer-scraper/', RunKupferScraperView.as_view(), name='run-kupfer-scraper'),
    path('run-all-scrapers/', RunAllScrapersView.as_view(), name='run-all-scrapers'),
]
