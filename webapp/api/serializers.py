from rest_framework import serializers
from .models import People

class PeopleSerializer(serializers.Serializer):
	file_uploaded=serializers.FileField()