from django.urls import path
from .views import ScrapedDataList
from .views import RunKupferScraperView

urlpatterns = [
    path('scraped-data/', ScrapedDataList.as_view(), name='scraped-data-list'),
    path('run-kupfer-scraper/', RunKupferScraperView.as_view(), name='run-kupfer-scraper'),
]