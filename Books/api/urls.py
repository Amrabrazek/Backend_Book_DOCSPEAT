from django.urls import path
from .views import User_list,User_details,Author_list,Author_details,Reader_list,Reader_details,Reader_books_list,Reader_books_details,Book_list,Book_details,Page_list,Page_details

app_name = 'api'


urlpatterns=[
    
    path('user/', User_list, name='UsersInfo'),
    path('user/<int:id>',User_details, name='UsersDetails' ),

    path('author/', Author_list.as_view(), name='Authorinfo'),
    path('author/<int:pk>',Author_details.as_view(), name='AuthorsDetails' ),

    path('reader/', Reader_list, name='Readerinfo'),
    path('reader/<int:id>',Reader_details, name='ReaderDetails' ),

    path('reader_books/', Reader_books_list, name='Readerbooksinfo'),
    path('reader_books/<int:id>',Reader_books_details, name='ReaderbooksDetails' ),
    
    path('book/', Book_list.as_view(), name='BooksInfo'),
    path('book/<int:pk>',Book_details.as_view(), name='BooksDetails' ),
    
    path('page/', Page_list, name='PageInfo'),
    path('page/<int:id>',Page_details, name='PageDetails' ),
]