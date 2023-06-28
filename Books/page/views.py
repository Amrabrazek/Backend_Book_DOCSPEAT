from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import  IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions, AllowAny, IsAuthenticated
from .models import Book, Page
from .serializers import PageSerializer, PagesSerializer
from rest_framework.decorators import api_view
from .permissions import OwnerOfTheBookOrReadOnly
from rest_framework.decorators import api_view,permission_classes
from django.http import Http404

# my views.


class Page_list(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class Page_details(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class PageCreate(generics.CreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticated]

class PageUpdate(generics.UpdateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticated, OwnerOfTheBookOrReadOnly]

class PageDelete(generics.DestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticated, OwnerOfTheBookOrReadOnly]

# endpoint to list all tha author posts
@api_view(['GET'])
@permission_classes([OwnerOfTheBookOrReadOnly])
def BookPages(request,pk):
    if request.method == 'GET':
        try:
            book = Book.objects.get(id = pk)
            pages = Page.objects.filter(book=book)
            serializer = PagesSerializer(pages, many=True)
        except Book.DoesNotExist:
            raise Http404("Book not found")
    return Response(serializer.data, status=status.HTTP_200_OK)

