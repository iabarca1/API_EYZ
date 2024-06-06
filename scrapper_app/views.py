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
        try:
            run_all_scrapers()
            return Response({"status": "All scrapers run successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)