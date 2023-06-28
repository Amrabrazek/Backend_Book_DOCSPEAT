from django.shortcuts import render, redirect
from rest_framework import status, generics
from rest_framework.permissions import  IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions, AllowAny, IsAuthenticated
from .models import  Reader_books, Book
from users.models import CustomUser
from .serializers import BookSerializer, ReaderbookSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.decorators import api_view,permission_classes
from django.http import Http404
from rest_framework.response import Response
# my views.


class Book_list(generics.ListAPIView):
    premission_classes = (IsAuthenticated, )
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class Book_details(generics.RetrieveAPIView):
    premission_classes = (IsAuthenticated, )
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdate(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

class BookDelete(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class Reader_book(generics.ListCreateAPIView):
    premission_classes = (IsAuthenticated, )
    queryset = Reader_books.objects.all()
    serializer_class = ReaderbookSerializer

# endpoint to list all tha author posts
@api_view(['GET'])
@permission_classes([IsAuthorOrReadOnly])
def AuthorBook(request,pk):
    if request.method == 'GET':
        try:
            owner = CustomUser.objects.get(id = pk)
            authorBooks = owner.author_books.all()
            serializer = BookSerializer (authorBooks, many = True)
        except Book.DoesNotExist:
            raise Http404("User not found")
    return Response(serializer.data, status=status.HTTP_200_OK)


# endpoint to list all tha author posts
@api_view(['GET'])
@permission_classes([IsAuthorOrReadOnly])
def BookReader(request,pk):
    if request.method == 'GET':
        try:
            book = Reader_books.objects.get(id = pk)
            bookReaders = book.author_books.all()
            serializer = BookSerializer (bookReaders, many = True)
        except Book.DoesNotExist:
            raise Http404("User not found")
    return Response(serializer.data, status=status.HTTP_200_OK)
