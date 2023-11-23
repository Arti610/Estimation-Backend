from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import *


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id","first_name","last_name","email","phone_number","profile_image","date_joined","department","account_status","address","user_type",'last_login']
    
    
class CustomUserSerializer1(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id","first_name","last_name","email","phone_number","profile_image","date_joined","department","account_status","address","user_type",'last_login']
        depth=1



class CustomUserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["first_name","last_name","email","phone_number","profile_image","date_joined","department","account_status","address","user_type","password",'last_login']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = get_user_model()(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

   
class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["first_name","last_name","email","phone_number","profile_image","date_joined","department","account_status","address","user_type"]

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value
    
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields='__all__'
        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields='__all__'
        
    
class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value
