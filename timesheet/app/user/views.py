from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from . models import Userdetails
from . serializers import userSerializer

class userList(APIView):

	def get(self,request):
		user1=Userdetails.objects.all()
		serializer=userSerializer(user1,many=True)
		return Response(serializer.data,status=status.HTTP_200_OK)

	def post(self,request):
		user1=Userdetails.objects.all()
		serializer=userSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response("Success!!!  Data is valid and posted",status=status.HTTP_201_CREATED)
		return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class Test(APIView):
# 	def get(self, request):
# 	    return Response("Hello, world. You're at the polls index.",status=status.HTTP_200_OK)