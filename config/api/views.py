from django.shortcuts import render
from .serializers import SuperMarketSerializer
from .models import SuperMarket
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

class SuperMarketViewSet(viewsets.ModelViewSet):
    serializer_class = SuperMarketSerializer
    queryset = SuperMarket.objects.all()
    http_method_names = ['get', 'post', 'patch', 'put', 'delete',]
