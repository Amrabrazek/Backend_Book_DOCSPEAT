from django.urls import path ,re_path
from .views import Page_list,Page_details, PageCreate, PageUpdate, PageDelete, BookPages


urlpatterns=[
    
    path('', Page_list.as_view(), name='PageInfo'),
    path('<int:pk>',Page_details.as_view(), name='PageDetails' ),

    path('create', PageCreate.as_view(), name='pagecreate'),
    path('update/<int:pk>', PageUpdate.as_view(), name='pageupdate'),
    path('delete/<int:pk>', PageDelete.as_view(), name='pagedelete'),

    # all the books that belong to the author of id = pk
    path('authorbooks/<int:pk>/', BookPages, name='bookpages'),
]