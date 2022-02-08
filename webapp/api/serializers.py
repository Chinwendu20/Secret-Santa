from rest_framework import serializers
from .models import People
from django.core.validators import FileExtensionValidator

class PeopleSerializer(serializers.Serializer):
	file_uploaded=serializers.FileField(validators=[FileExtensionValidator(allowed_extensions=['xlsx', 'csv'])])

# class Data_People(serializers.ModelSerializer):
# 	class Meta:
# 		model=People
# 		fields='__all__'

