from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .scrapers.run_all_scrapers import run_all_scrapers

class RunAllScrapersView(APIView):
    def get(self, request, format=None):
        try:
            results = run_all_scrapers()
            return Response({"status": "All scrapers run successfully", "results": results}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
