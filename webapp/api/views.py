from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import PeopleSerializer
from django.core.files.storage import FileSystemStorage
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework import status
import pandas
import random
# Create your views here.

class FileUpload(APIView):
	serializer_class=PeopleSerializer
	def post(self, request):
		serializer=self.serializer_class(data=request.data)
		if serializer.is_valid():
			file_uploaded=request.FILES['file_uploaded']
			# file_uploaded=serializer.data['file_uploaded']
			# print('serializer')
			# print(serializer)
			# print('Serializer.data')
			# print(serializer.data)
			Saved_People_data=FileSystemStorage().save(file_uploaded, file_uploaded)
			People_url=FileSystemStorage().url(Saved_People_data)
			# People_data=pandas.read_excel('.'+ People_url)
			# length_of_data=People_data.shape[0]
			# random_list=random.sample(range(1,length_of_data+1), length_of_data)
			# for row in People_data.itertuples():
			# 			print(People_data.index)
			# 			People.objects.create(NAME=People_data.NAME, EMAIL=People_data.EMAIL)
			# length_of_frame=People_data.shape[0]
			# if length_of_frame%2 == 0:
			# 	list_of_random_numbers=random.sample(range(1,length_of_frame+1), length_of_frame)
				# print('NAME-{}----EMAIL-{}'.format(People_data.NAME, People_dat))
			# print(People_data)
			content = {'response': People_url}

			return Response(content, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ShowMatchingView(APIView):
	
	def get (self, request, slug):
			People_data=pandas.read_excel('./'+ slug)
			length_of_data=People_data.shape[0]
			if length_of_data % 2 != 0:
				content={'Warning': 'One person would be left without a match'}
				return Response(content, status=status.HTTP_200_OK)
			random_list=random.sample(range(1,length_of_data+1), length_of_data)
			content=[]
			i=0
			end=length_of_data-1
			while i<=end:
				content.append({'NAME': People_data.NAME[i],
								'EMAIL': People_data.EMAIL[i],
								'Match_Pair':i+1})
				i=i+2

			return Response(content, status=status.HTTP_200_OK)

class ShowDataView(APIView):

	def get(self, request, slug, pk):
		People_data=pandas.read_excel('./'+ slug)
		content={'NAME': People_data.iloc[pk].NAME,
				'EMAIL': People_data.iloc[pk].EMAIL}

		return Response(content, status=status.HTTP_200_OK)

