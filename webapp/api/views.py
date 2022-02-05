from django.shortcuts import render
from rest_framework import APIView
from .serializers import PeopleSerializer
from django.core.files.storage import FileSystemStorage

# Create your views here.

def FileUpload(APIView):
	serializer_class=PeopleSerializer

	def post(self, request, format=None):
		file_uploaded=request.FILES['file_uploaded']
		Saved_People_data=FileSystemStorage().save(People.xsl, file_uploaded)
 		People_url=FileSystemStorage().url(file_uploaded)
 		People_data=pandas.read_csv('.'+People_url)
 		for row in People_data.itertuples():
 					People.objects.create(Name=People_data.Name, Email=People_data.Email)
