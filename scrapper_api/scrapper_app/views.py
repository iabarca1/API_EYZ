# scraper_app/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .scrapers.kupfer4 import run_kupfer_scraper  # Asegúrate de que run_kupfer_scraper esté definido en kupfer4.py

class RunKupferScraperView(APIView):
    def get(self, request, format=None):
        run_kupfer_scraper()
        return Response({"status": "Kupfer scraper run successfully"}, status=status.HTTP_200_OK)
