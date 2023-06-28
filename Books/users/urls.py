from django.urls import path ,re_path
from .views import User_list,User_details, HomeView, Register, activate, Logout, resetPassword, getResetPasswordLink
from rest_framework_simplejwt import views as jwt_views


urlpatterns=[
    
    path('', User_list.as_view(), name='UsersInfo'),
    path('<int:pk>',User_details.as_view(), name='UsersDetails' ),

    path('home/', HomeView.as_view(), name ='home'),

    path('register/', Register.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate.as_view(), name='activate'),

    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),

    path('resetpassword/(?P<uid>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', resetPassword, name='resetpassword'),
    path('resetpasswordlink/', getResetPasswordLink, name='resetpasswordlink'),

]