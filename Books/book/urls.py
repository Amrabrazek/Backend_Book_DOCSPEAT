from django.urls import path ,re_path
from .views import Book_list,Book_details, AuthorBook, BookCreate, BookUpdate, BookDelete


urlpatterns=[
    
    path('', Book_list.as_view(), name='BooksInfo'),
    path('<int:pk>',Book_details.as_view(), name='BooksDetails' ),
    path('create', BookCreate.as_view(), name='postcreate'),
    path('update/<int:pk>', BookUpdate.as_view(), name='postupdate'),
    path('delete/<int:pk>', BookDelete.as_view(), name='postdelete'),
    # path('likes', Like_list.as_view(), name='postlikes'),
    path('authorbooks/<int:pk>/', AuthorBook),

]