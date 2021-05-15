from rest_framework import serializers
from .models import AppData


class AppDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppData
        fields = ('id', 'name', 'trg', 'hservers', 'pservers', 'created_at')
