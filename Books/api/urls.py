from django.urls import path
from api import views

urlpatterns=[
    
    path('user/', views.User_list, name='UsersInfo'),
    path('user/<int:id>',views.User_details, name='UsersDetails' ),

    path('author/', views.Author_list, name='Authorinfo'),
    path('author/<int:id>',views.Author_details, name='AuthorsDetails' ),

    path('reader/', views.Reader_list, name='Readerinfo'),
    path('reader/<int:id>',views.Reader_details, name='ReaderDetails' ),

    path('reader_books/', views.Reader_books_list, name='Readerbooksinfo'),
    path('reader_books/<int:id>',views.Reader_books_details, name='ReaderbooksDetails' ),
    
    path('book/', views.Book_list, name='BooksInfo'),
    path('book/<int:id>',views.Book_details, name='BooksDetails' ),
    
    path('page/', views.Page_list, name='BooksInfo'),
    path('page/<int:id>',views.Page_details, name='BooksDetails' ),
]