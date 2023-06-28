from rest_framework import serializers
from django.utils import timezone
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if validate_password(validated_data['password']) == None:
            password = make_password(validated_data['password'])
            user = CustomUser.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                password=password,
                usertype=validated_data['usertype'],
            )
            return user
        

class PasswordUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['password']
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        if not validate_password(validated_data['password']):
            instance.password = make_password(validated_data['password'])
            instance.is_reset = False
            instance.save()
            return instance

# class UserBookPageSerializer(serializers.Serializer):

#     author = UserSerializer()
#     book = BookSerializer()
#     page = PageSerializer()

#     def to_representation(self, instance):
#         data = super(UserBookPageSerializer, self).to_representation(instance)
#         return {'user': data['user'], 'book': data['book'], 'page': data['page']}
