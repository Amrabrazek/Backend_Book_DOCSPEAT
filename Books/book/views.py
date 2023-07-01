from django.shortcuts import render, redirect
from rest_framework import status, generics
from rest_framework.permissions import  IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions, AllowAny, IsAuthenticated
from .models import  Reader_books, Book
from users.models import CustomUser
from .serializers import BookSerializer, ReaderbookSerializer,BookSerializer2, ReaderBooksSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.decorators import api_view,permission_classes
from django.http import Http404
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# my views.


class Book_list(generics.ListAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class Book_details(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Book.objects.all()
    serializer_class = BookSerializer2

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

class Reader_book_list(generics.ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Reader_books.objects.all()
    serializer_class = ReaderBooksSerializer


class Reader_book(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = Reader_books.objects.all()
    serializer_class = ReaderbookSerializer

# endpoint to list all tha author books
@api_view(['GET'])
@permission_classes([IsAuthorOrReadOnly])
def AuthorBooks(request,pk):
    if request.method == 'GET':
        try:
            owner = CustomUser.objects.get(id = pk)
            authorBooks = owner.author_books.all()
            serializer = BookSerializer (authorBooks, many = True)
        except CustomUser.DoesNotExist:
            raise Http404("User not found")
    return Response(serializer.data, status=status.HTTP_200_OK)


# endpoint to list all tha reader books
@api_view(['GET'])
@permission_classes([IsAuthorOrReadOnly])
def ReaderBooks(request,pk):
    if request.method == 'GET':
        try:
            reader = CustomUser.objects.get(id = pk)
            print(reader)
            readerbooks = reader.reader_books.all()
            print("-----------------------")
            print(readerbooks)
            serializer = BookSerializer (readerbooks, many = True)
        except Book.DoesNotExist:
            raise Http404("User not found")
    return Response(serializer.data, status=status.HTTP_200_OK)

# @api_view(['GET'])
# @permission_classes([IsAuthorOrReadOnly])
# def ReaderBooks(request, pk):
#     try:
#         reader = CustomUser.objects.get(id=pk, usertype='reader')
#         books = reader.reader_books.all().values_list('book', flat=True)
#         book_objects = Book.objects.filter(id__in=books)
#         serializer = BookSerializer(book_objects, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except CustomUser.DoesNotExist:
#         raise Http404("User not found")

class ReaderBooks(generics.ListAPIView):
    serializer_class = ReaderBooksSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(CustomUser, id=user_id, usertype='reader')
        queryset = Reader_books.objects.filter(reader=user)
        return queryset

# @api_view(['GET'])
# @permission_classes([AllowAny])
# def ReaderBooks(request, pk):
#     try:
#         reader = CustomUser.objects.get(id=pk, usertype='reader')
#         print(reader)
#         reader_books = Reader_books.objects.filter(reader=reader)
#         print(reader_books)
#         books = [rb.book for rb in reader_books]
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except CustomUser.DoesNotExist:
#         raise Http404("User not found")