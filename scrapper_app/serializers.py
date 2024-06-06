# scrapper_app/serializers.py

from rest_framework import serializers
from scrapper_app.models import ScrapedData

class ScrapedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapedData
        fields = '__all__'
