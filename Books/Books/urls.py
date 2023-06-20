"""
URL configuration for Books project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views.User_list, name='UsersInfo'),
    path('user/<int:id>',views.User_details, name='UsersDetails' ),
    path('book/', views.Book_list, name='BooksInfo'),
    path('book/<int:id>',views.Book_details, name='BooksDetails' ),
    path('page/', views.Page_list, name='BooksInfo'),
    path('page/<int:id>',views.Page_details, name='BooksDetails' ),
    


]
