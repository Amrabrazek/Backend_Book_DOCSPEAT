from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import  IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions, AllowAny, IsAuthenticated
from .models import Book, Page
from .serializers import PageSerializer
from rest_framework.decorators import api_view

from django.views.decorators.csrf import csrf_exempt
# my views.


class Page_list(generics.ListCreateAPIView):
    premission_classes = (IsAuthenticated, )
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class Page_details(generics.RetrieveUpdateDestroyAPIView):
    premission_classes = (IsAuthenticated, )
    queryset = Page.objects.all()
    serializer_class = PageSerializer


class BookPages(APIView):
    def get(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        pages = Page.objects.filter(book=book)
        serializer = PageSerializer(pages, many=True)
        return Response(serializer.data)
    

class Page_details(generics.RetrieveUpdateDestroyAPIView):
    premission_classes = (IsAuthenticated, )
    queryset = Page.objects.all()
    serializer_class = PageSerializer