# scrapper_app/views.py
# scrapper_app/views.py

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scrapper_app.models import ScrapedData
from scrapper_app.serializers import ScrapedDataSerializer
from scrapper_app.scrapers.kupfer4 import run_kupfer_scraper
from scrapper_app.scrapers.run_all_scrapers import run_all_scrapers
from .tasks import run_all_scrapers_task

class ScrapedDataList(generics.ListCreateAPIView):
    queryset = ScrapedData.objects.all()
    serializer_class = ScrapedDataSerializer

class RunKupferScraperView(APIView):
    def get(self, request, format=None):
        run_kupfer_scraper()
        return Response({"status": "Kupfer scraper run successfully"}, status=status.HTTP_200_OK)

class RunAllScrapersView(APIView):
    def get(self, request, format=None):
        run_all_scrapers_task.delay()
        return Response({"status": "Scrapers are running in the background"}, status=status.HTTP_200_OK)