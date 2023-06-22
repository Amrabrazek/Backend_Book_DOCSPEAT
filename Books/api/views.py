from django.shortcuts import render
from rest_framework import status, generics,  viewsets 
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from api.models import User, Author, Reader, Reader_books, Book, Page
from .serializers import UserSerializer,AuthorSerializer,ReaderSerializer,BookSerializer,ReaderbookSerializer,PageSerializer,UserBookPageSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser
# my views.

# Users views 
# list all users 
@api_view(['GET', 'POST'])
def User_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializeredUsers = UserSerializer(users, many=True)
        return Response(serializeredUsers.data)
    if request.method == 'POST':
        serializeredUsers = UserSerializer(data = request.data)
        if serializeredUsers.is_valid():
            serializeredUsers.save()
            return Response(serializeredUsers.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializeredUsers.data, status = status.HTTP_400_BAD_REQUEST)

# list, edit or delete user
@api_view(['GET', 'PUT', 'DELETE'])
def User_details(request, id):
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializeredUsers = UserSerializer(user)
        return Response(serializeredUsers.data)
        # return JsonResponse({"Users": serializeredUsers.data} , safe=False)

    elif request.method == 'PUT':
        serializeredUsers = UserSerializer(user, data = request.data)
        if serializeredUsers.is_valid():
            serializeredUsers.save()
            return Response(serializeredUsers.data )
        return Response(serializeredUsers.errors, status=status.HTTP_400_BAD_REQUEST )
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# -------------------------------------------------------------

# Author views 
# # list all authors 
# @api_view(['GET', 'POST'])
# def Author_list(request):
#     if request.method == 'GET':
#         authors = Author.objects.all()
#         serializeredAuthors = AuthorSerializer(authors, many=True)
#         return Response(serializeredAuthors.data)
#     if request.method == 'POST':
#         serializeredAuthors = AuthorSerializer(data = request.data)
#         if serializeredAuthors.is_valid():
#             serializeredAuthors.save()
#             return Response(serializeredAuthors.data, status = status.HTTP_201_CREATED)
#         else:
#             return Response(serializeredAuthors.data, status = status.HTTP_400_BAD_REQUEST)

# # list, edit or delete user
# @api_view(['GET', 'PUT', 'DELETE'])
# def Author_details(request, id):
#     try:
#         author = Author.objects.get(id=id)
#     except Author.DoesNotExist:
#         return Response (status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializeredAuthor = AuthorSerializer(author)
#         return Response(serializeredAuthor.data)
#         # return JsonResponse({"Users": serializeredUsers.data} , safe=False)

#     elif request.method == 'PUT':
#         serializeredAuthor = AuthorSerializer(author, data = request.data)
#         if serializeredAuthor.is_valid():
#             serializeredAuthor.save()
#             return Response(serializeredAuthor.data )
#         return Response(serializeredAuthor.errors, status=status.HTTP_400_BAD_REQUEST )
    
#     elif request.method == 'DELETE':
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class Author_list(generics.ListCreateAPIView):
    premission_classes = [IsAdminUser]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class Author_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
# -------------------------------------------------------------

# reader views 
# list all authors 
@api_view(['GET', 'POST'])
def Reader_list(request):
    if request.method == 'GET':
        readers = Reader.objects.all()
        serializeredReaders = ReaderSerializer(readers, many=True)
        return Response(serializeredReaders.data)
    if request.method == 'POST':
        serializeredReaders = ReaderSerializer(data = request.data)
        if serializeredReaders.is_valid():
            serializeredReaders.save()
            return Response(serializeredReaders.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializeredReaders.data, status = status.HTTP_400_BAD_REQUEST)

# list, edit or delete user
@api_view(['GET', 'PUT', 'DELETE'])
def Reader_details(request, id):
    try:
        readers = Reader.objects.get(id=id)
    except Reader.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializeredReader = ReaderSerializer(readers)
        return Response(serializeredReader.data)
        # return JsonResponse({"Users": serializeredUsers.data} , safe=False)

    elif request.method == 'PUT':
        serializeredReader = ReaderSerializer(readers, data = request.data)
        if serializeredReader.is_valid():
            serializeredReader.save()
            return Response(serializeredReader.data )
        return Response(serializeredReader.errors, status=status.HTTP_400_BAD_REQUEST )
    
    elif request.method == 'DELETE':
        Reader.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# -------------------------------------------------------------


class Book_list(generics.ListCreateAPIView):
    premission_classes = (IsAdminUser )
    queryset = Book.objects.all()
    print(queryset)
    serializer_class = BookSerializer


class Book_details(generics.RetrieveUpdateDestroyAPIView):
    premission_classes = (IsAdminUser )
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class MyModelViewSet(viewsets.ModelViewSet):
#     queryset = MyModel.objects.order_by('-creation_date')
#     serializer_class = MyModelSerializer
#     parser_classes = (MultiPartParser, FormParser)
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(creator=self.request.user)


def upload_image(request):
    if request.method == 'POST' and request.FILES['book_cover']:
        myfile = request.FILES['book_cover']
        fs = FileSystemStorage()
        filename = fs.save('book_images/' + myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return JsonResponse({'url': uploaded_file_url})
    return JsonResponse({'error': 'Invalid request'})
# -------------------------------------------------------------

# Reader_books views 
# list all reader and books
@api_view(['GET', 'POST'])
def Reader_books_list(request):
    if request.method == 'GET':
        reader_books = Reader_books.objects.all()
        serializeredReaderBooks = ReaderbookSerializer(reader_books, many=True)
        return Response(serializeredReaderBooks.data)
    if request.method == 'POST':
        serializeredReaderBooks = ReaderbookSerializer(data = request.data)
        if serializeredReaderBooks.is_valid():
            serializeredReaderBooks.save()
            return Response(serializeredReaderBooks.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializeredReaderBooks.data, status = status.HTTP_400_BAD_REQUEST)

# list, edit or delete realtion
@api_view(['GET', 'PUT', 'DELETE'])
def Reader_books_details(request, id):
    try:
        reader_books = Reader_books.objects.get(id=id)
    except Reader_books.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializeredReaderBooks = ReaderbookSerializer(reader_books)
        return Response(serializeredReaderBooks.data)
        # return JsonResponse({"Books": serializeredBooks.data} , safe=False)

    elif request.method == 'PUT':
        serializeredReaderBooks = ReaderbookSerializer(reader_books, data = request.data)
        if serializeredReaderBooks.is_valid():
            serializeredReaderBooks.save()
            return Response(serializeredReaderBooks.data )
        return Response(serializeredReaderBooks.errors, status=status.HTTP_400_BAD_REQUEST )
    
    elif request.method == 'DELETE':
        reader_books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# -------------------------------------------------------------

# Pages views 
# list all books
@api_view(['GET', 'POST'])
def Page_list(request):
    if request.method == 'GET':
        pages = Page.objects.all()
        serializeredPages = PageSerializer(pages, many=True)
        return Response(serializeredPages.data)
    if request.method == 'POST':
        serializeredPages = PageSerializer(data = request.data)
        if serializeredPages.is_valid():
            serializeredPages.save()
            return Response(serializeredPages.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializeredPages.data, status = status.HTTP_400_BAD_REQUEST)

# list, edit or delete user
@api_view(['GET', 'PUT', 'DELETE'])
def Page_details(request, id):
    try:
        page = Page.objects.get(id=id)
    except Page.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializeredPages = PageSerializer(page)
        return Response(serializeredPages.data)
        # return JsonResponse({"Pages": serializeredPages.data} , safe=False)

    elif request.method == 'PUT':
        serializeredPages = PageSerializer(page, data = request.data)
        if serializeredPages.is_valid():
            serializeredPages.save()
            return Response(serializeredPages.data )
        return Response(serializeredPages.errors, status=status.HTTP_400_BAD_REQUEST )
    
    elif request.method == 'DELETE':
        page.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


