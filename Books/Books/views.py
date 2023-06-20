from django.http import JsonResponse
from django.shortcuts import render
from .models import User, Book, Page
from .serializers import UserSerializer,BookSerializer,PageSerializer,UserBookPageSerializer 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics



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


# Books views 
# list all books
@api_view(['GET', 'POST'])
def Book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializeredBooks = BookSerializer(books, many=True)
        return Response(serializeredBooks.data)
    if request.method == 'POST':
        serializeredBooks = BookSerializer(data = request.data)
        if serializeredBooks.is_valid():
            serializeredBooks.save()
            return Response(serializeredBooks.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializeredBooks.data, status = status.HTTP_400_BAD_REQUEST)

# list, edit or delete user
@api_view(['GET', 'PUT', 'DELETE'])
def Book_details(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializeredBooks = BookSerializer(book)
        return Response(serializeredBooks.data)
        # return JsonResponse({"Books": serializeredBooks.data} , safe=False)

    elif request.method == 'PUT':
        serializeredBooks = BookSerializer(book, data = request.data)
        if serializeredBooks.is_valid():
            serializeredBooks.save()
            return Response(serializeredBooks.data )
        return Response(serializeredBooks.errors, status=status.HTTP_400_BAD_REQUEST )
    
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


# class UserBookPageView(generics.RetrieveAPIView):
#     serializer_class = UserBookPageSerializer

#     def get(self, request, *args, **kwargs):
#         # Get user, book, and page data from the database
#         user = request.user
#         book = Book.objects.get(id=kwargs['book_id'])
#         page = Page.objects.get(id=kwargs['page_id'])

#         # Create a dictionary with the data to be serialized
#         data = {
#             'user': user,
#             'book': book,
#             'page': page,
#         }

#         # Create an instance of the serializer with the data
#         serializer = UserBookPageSerializer(data=data)

#         # Serialize the data and return it as a JSON response
#         return Response(serializer.data)