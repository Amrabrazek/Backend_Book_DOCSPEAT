from django.shortcuts import render, redirect
from rest_framework import status, generics,  viewsets 
from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions, AllowAny, IsAuthenticated
from .models import CustomUser
from .serializers import UserSerializer, SignupSerializer, PasswordUpdateSerializer
from .permissions import IsAccountOwner
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
# my views.
#FWT
from rest_framework.views import APIView
from django.utils.deprecation import MiddlewareMixin

from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token  , password_reset_token
from django.core.mail import EmailMessage


class User_list(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class User_details(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserUpdate(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAccountOwner]

class UserDelete(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAccountOwner]


class AuthorList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(usertype='author')


class ReaderList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(usertype='reader')

# JWT TOKEN
class HomeView(APIView):
    permission_classes = ( IsAuthenticated, )
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            content = {'msg':  {user.id} }
        else:
            content = {'msg': "User not authenticated"}
        return Response(content)


# email activation 
class Register(APIView):
    def post(self, request):
        password = request.data.get('password', None)
        confirm_password = request.data.get('confirm_password', None)
        if not password == confirm_password:
            return Response({'password_mismatch': 'Password fields did not match'}, status.HTTP_400_BAD_REQUEST)
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = serializer.data
        # current_site = get_current_site(request)  
        current_site = "127.0.0.1:8000"  
        print(current_site)
        mail_subject = 'Books account activation'  
        message = render_to_string('acc_active_email.html', {  
            'user': user,  
            'domain': current_site,
            'uid':urlsafe_base64_encode(bytes(str(user.pk),'utf-8')),  
            'token':account_activation_token.make_token(user),  
            
        })  
        print(message)
        to_email = [user.email] 
        print (to_email)
        email = EmailMessage(mail_subject, message, to=to_email)
        print (email)

        email.send()
        return Response(data, status=status.HTTP_201_CREATED)


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        


class activate(APIView):
    def get(self, request, uidb64, token):
        id = urlsafe_base64_decode(uidb64)
        id = id.decode('utf-8')
        try:
            user = CustomUser.objects.get(pk=id)
            if account_activation_token.check_token(user, token):
                user.is_active = True
                user.save()
                return Response({"msg": "Account Activated"}, status.HTTP_200_OK)            
            return Response({"msg": "Account is already Activated"}, status.HTTP_200_OK)
        except(TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            return Response({"msg": "Activation link is invalid"}, status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def getResetPasswordLink(request):
    email = request.data.get('email', None)

    if not email:
        return Response({"msg": "no email was provided"}, status.HTTP_400_BAD_REQUEST)
    
    try:
        user = CustomUser.objects.get(email=request.data['email'])
        user.is_reset = True
        user.save()
        token = password_reset_token.make_token(user)
        
        current_site = get_current_site(request)  
        mail_subject = 'Password Reset'  
        message = render_to_string('password_reset.html', {  
            'user': user,
            'domain': current_site.domain,  
            'uid':urlsafe_base64_encode(bytes(str(user.pk),'utf-8')),  
            'token': token  
        })  
        to_email = [user.email]
        email = EmailMessage(mail_subject, message, to=to_email)

        email.send()
        print(user.pk)
        uid = urlsafe_base64_encode(bytes(str(7),'utf-8'))
        print(uid, urlsafe_base64_decode(uid).decode('utf-8'))
        return Response({"msg": f"we have sent an reset link to {user.email}"})
    except Exception as e:
        return Response({"msg": f"{e}"}, status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST', 'GET'])
def resetPassword(request, uid, token):
    id = urlsafe_base64_decode(uid).decode('utf-8')
    try:
        user = CustomUser.objects.get(pk=id)   
        passowrd = request.data.get('password', None)
        confrim_password = request.data.get('confirm_password', None)
        print(password_reset_token.check_token(user, token))
        if not password_reset_token.check_token(user, token):
            return Response({'msg': 'invalid link'}, status.HTTP_400_BAD_REQUEST)
        if not passowrd or not confrim_password:
            return Response({'msg': 'missing data'}, status.HTTP_400_BAD_REQUEST)
        if not passowrd == confrim_password:
            return Response({'msg': 'passowrds did not match'}, status.HTTP_400_BAD_REQUEST)
        
        serializer = PasswordUpdateSerializer(instance=user, data=request.data , partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({"msg":"password was reset"})
        
    except Exception as e:
        return Response({"msg": e}, status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class CorsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = 'http://localhost:3000'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response

