from django.urls import path ,re_path
from .views import Book_list,Book_details, BookCreate, BookUpdate, BookDelete, AuthorBooks, ReaderBooks


urlpatterns=[
    
    path('', Book_list.as_view(), name='BooksInfo'),
    path('<int:pk>',Book_details.as_view(), name='BooksDetails' ),

    path('create', BookCreate.as_view(), name='bookcreate'),
    path('update/<int:pk>', BookUpdate.as_view(), name='bookupdate'),
    path('delete/<int:pk>', BookDelete.as_view(), name='bookdelete'),

    # all the books that belong to the author of id = pk
    path('authorbooks/<int:pk>/', AuthorBooks),

    # all the books that reader of id = pk read
    path('readersbooks/<int:pk>/', ReaderBooks),

]