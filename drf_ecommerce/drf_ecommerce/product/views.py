from django.shortcuts import render

# Create your views here.

from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer,ProductLineSerializer
from rest_framework.response import Response

# Create your views here.
from .models import Category, Product, Brand,ProductLine


class CategoryView(viewsets.ViewSet):

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandView(viewsets.ViewSet):

    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductView(viewsets.ViewSet):

    queryset = Product.objects.all()

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
class ProductLineView(viewsets.ViewSet):
    queryset=ProductLine.objects.all()

    @extend_schema(responses=ProductLineSerializer)
    def list(self,request):
        serializer =ProductLineSerializer(self.queryset,many=True)
        return Response(serializer.data)
