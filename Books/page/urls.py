from django.urls import path ,re_path
from .views import Page_list,Page_details


urlpatterns=[
    
    path('', Page_list.as_view(), name='PageInfo'),
    path('<int:pk>',Page_details.as_view(), name='PageDetails' ),

]