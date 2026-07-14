from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import viewsets
import requests
from django.http import HttpResponse

class item_api(APIView):
    def post(self,request):
        try:
            serializer = itemSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"created successfully" , "data": serializer.data}, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({"message":"fail to create" , "error":str(e)} , status=status.HTTP_400_BAD_REQUEST)
        
    def get(self , request , pk=None):
        try:
            if pk == None:
                items = item.objects.all()
                serializer = itemSerializer(items , many = True)
                return Response({"message":"created" , "data" : serializer.data}, status=status.HTTP_200_OK)
            else:
                items = item.objects.get(pk=pk)
                serializer = itemSerializer(items)
                return Response({"message":"created" , "data" : serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message" :"failed" ,"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request , pk=None):
        try:
            items = item.objects.get(pk=pk)
            serializer = itemSerializer(items,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"created successfully" , "data": serializer.data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message" :"failed" ,"error":str(e)},status=status.HTTP_400_BAD_REQUEST)  

    def delete(self , request , pk =None):
        try:
            items = item.objects.get(pk=pk) 
            items.delete()
            return Response({"message":"deleted successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message" :"failed" ,"error":str(e)},status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET' , 'POST' , 'PUT' , 'DELETE'])
def prd_fun(request ,  pk=None):
    if request.method == 'POST':
        try:
            serializer = itemSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"created successfully" , "data": serializer.data}, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({"message":"fail to create" , "error":str(e)} , status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
         try:
            if pk == None:
                items = item.objects.all()
                serializer = itemSerializer(items , many = True)
                return Response({"message":"created" , "data" : serializer.data}, status=status.HTTP_200_OK)
            else:
                items = item.objects.get(pk=pk)
                serializer = itemSerializer(items)
                return Response({"message":"created" , "data" : serializer.data}, status=status.HTTP_200_OK)
         except Exception as e:
            return Response({"message" :"failed" ,"error":str(e)},status=status.HTTP_400_BAD_REQUEST)

class prd_gen(generics.CreateAPIView):
    queryset = item.objects.all()
    serializer_class = itemSerializer
class prod_crt(generics.ListCreateAPIView):
    queryset = item.objects.all()
    serializer_class = itemSerializer


class prd_view(viewsets.ModelViewSet):
    queryset = item.objects.all()
    serializer_class = itemSerializer
    
    
    def get_queryset(self):
      return item.objects.filter(user = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

@api_view(['POST'])
def signup(request):
    serializer = SignupSerializer(data = request.data)
    if serializer.is_valid():
                serializer.save()
                return Response({"message":"created successfully" , "data": serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors)
                         
def get_dummy_data(request):
    result = requests.get("https://dummyjson.com/users")
    res = result.json()
    print(res)
    return HttpResponse("hiiii")



