from django.shortcuts import render
from .models import Student
from .services import Student_serilizer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.contrib.auth.models import User
# Create your views here.

class Student_view(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,format=None):
        user=request.user
        stu  = Student.objects.filter(user=user)
        seri = Student_serilizer(stu,many=True)
        return Response(seri.data)
    def post(self,request,format=True):
        seri = Student_serilizer(data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data, status=status.HTTP_201_CREATED)
        return Response(seri.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        snippet =  Student.objects.get(pk)
        serializer = Student_serilizer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        data = Student.objects.get(pk=pk)
        print(data,'-----------')
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # queryset = Student.objects.all()
    # serializer_class = Student_serilizer
    # # authentication_classes = [JWTAuthentication]
    # # # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
   
  
    # # permission_classes = [AllowAny]


# http post http://127.0.0.1:8000/gettoken/ username=admin password=admin


# http http://127.0.0.1:8000/user/ "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYzNjA4MTE0LCJpYXQiOjE2NjM2MDc4MTQsImp0aSI6ImY0ZDRlOWYyMWM3MDRhM2Q4ZTQ0NTBlNThkMTlmZDI4IiwidXNlcl9pZCI6MX0.4PKzbdhRdvax0LVjLfnsaDlCOab0GG4PnT3nqQgQRVE"
