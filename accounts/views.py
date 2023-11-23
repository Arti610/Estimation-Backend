import random
from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListCreateAPIView,GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from accounts.authentication import MultiTokenAuthentication
from accounts.serializers import *
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.parsers import FormParser,MultiPartParser
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login,logout
from rest_framework import generics
from master.models import UserLog
from master.serializers import *
from master.models import UserLog
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

class UserRegistration(CreateAPIView):
    authentication_classes = []
    permission_classes = []
    # parser_classes = (MultiPartParser, FormParser)
    def post(self,request):
        try:
            customuser = CustomUserCreationSerializer(data=request.data)
            print('data....',request.data)
            print(request.data)
            if customuser.is_valid():
                user=customuser.save()
                UserLog.objects.create(user=CustomUser.objects.get(id=request.user.id), transactions_reference=f"User Created: {user.email}")
                print(customuser.data)
                return Response(customuser.data,status=status.HTTP_201_CREATED) 
            else:
                print('errors ',customuser.errors)
                return Response(customuser.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('erorr',e)
            print(":::",customuser.errors)
            return Response(customuser.errors,status=status.HTTP_400_BAD_REQUEST)


class CustomUserList(APIView):
    authentication_classes = [MultiTokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        qs = CustomUser.objects.all().exclude(is_superuser=True)
        customuser = CustomUserSerializer1(qs, many=True)       
        return Response(customuser.data,status=status.HTTP_200_OK)
    
    
class GetCustomUser(APIView):
    authentication_classes = [MultiTokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,id):
        try:
            res = CustomUser.objects.get(id=id)
            return Response(CustomUserSerializer1(res).data,status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            message = {"error":"Invalid User"}
            return Response(message,status=status.HTTP_404_NOT_FOUND)
        
        
# class StaffLogin(APIView):
#     def post(self, request):
#         email = request.data['email']
#         password = request.data['password']
#         try:
#             user = CustomUser.objects.get(email=email, user_type='Staff')
#             if user.check_password(password):
#                 user = authenticate(request, email=email, password=password)
#                 if user:
#                     login(request, user)
#                     token = MultiToken.objects.create(user=user)
#                     ser = CustomUserSerializer(user)
#                     context = {
#                         "data": ser.data,
#                         "token": token.key,
#                     }
#                     return Response(context, status=status.HTTP_202_ACCEPTED)
#             message = {"message": "Invalid Credential"}
#             return Response(message, status=status.HTTP_400_BAD_REQUEST)
#         except CustomUser.DoesNotExist:
#             message = {"message": "you are not a staff member"}
#             return Response(message, status=status.HTTP_400_BAD_REQUEST)        
class UserLogin(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self,request):
        print('........',request.data)
        email = request.data['email']
        password = request.data['password']
        try:
            user = authenticate(request,email=email,password=password)
            if user:
                login(request,user)
                # token = Token.objects.create(user=user)
                token = MultiToken.objects.create(user=user)
                ser = CustomUserSerializer(user)
                UserLog.objects.create(user=user, transactions_reference="User logged in")
                print("Token",token)
                context = {
                    "data":ser.data,
                    "token":token.key,
                }
                return Response(context,status=status.HTTP_202_ACCEPTED)
            else:
                message = {"message":"Invalid Credential"}
                return Response(message,status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            message = {"message":"Invalid Credential"}
            return Response(message,status=status.HTTP_400_BAD_REQUEST)
        
        
class UpdateUserProfile(APIView):
    authentication_classes = [MultiTokenAuthentication]
    permission_classes = [IsAuthenticated]
    # parser_classes = [MultiPartParser]
    def put(self, request,id):
        try:
            print(":::::::::::::::1",request.data)
            user=CustomUser.objects.get(id=id)
            ser=CustomUserSerializer(user,data=request.data,partial=True)
            if ser.is_valid():
                ser.save()
                print("::::::::::::::::::::::::2",ser.data)
                UserLog.objects.create(user=request.user, transactions_reference=f"User updated: {user}")
                return Response(ser.data,status=status.HTTP_201_CREATED)
            else:
                return Response(ser.data,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(":::::::::::::::::::3",e)
            return Response('error',status=status.HTTP_400_BAD_REQUEST)

class UserLogout(APIView):
    authentication_classes = [MultiTokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        # request.user.auth_token.delete()
        MultiToken.objects.get(user=request.user,key=request.data['key']).delete()
        logout(request)
        message = {"message":"logout successfully"}
        return Response(message,status=status.HTTP_200_OK)
    
    
    
class ChangePassword(APIView):
    authentication_classes = [MultiTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response({"old_password": ["Wrong password."]}, 
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            UserLog.objects.create(user=request.user, transactions_reference=f"Password changed")
            message = {"message":"Password Changed Successfully"}
            return Response(message,status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDelete(APIView):
    def delete(self, request,pk):
        user=CustomUser.objects.get(id=pk)
        user.delete()
        return Response('user deleted', status=status.HTTP_200_OK)

class CompanyAPI(APIView):
    authentication_classes = [MultiTokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        ser=CompanySerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request,pk=None):
        try:
            if pk is not None:
                company=Company.objects.get(id=pk)
                ser=CompanySerializer(company)
                return Response(ser.data,status=status.HTTP_200_OK)
            all_company=Company.objects.all()
            ser=CompanySerializer(all_company,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        except Company.DoesNotExist:
            print('Company does not exist')
            return Response('Company does not exist',status=status.HTTP_404_NOT_FOUND)
        
    
    def put(self,request,pk):
        try:
            company=Company.objects.get(id=pk)
            ser=CompanySerializer(company,data=request.data,partial=True)
            if ser.is_valid():
                ser.save()
                return Response(ser.data,status=status.HTTP_200_OK)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        except Company.DoesNotExist:
            msg='company does not exist'
            print(msg)
            return Response(msg,status=status.HTTP_400_BAD_REQUEST)
        
class DepartmentsAPI(APIView):
    def post(self,request):
        ser=DepartmentSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            UserLog.objects.create(user=request.user, transactions_reference=f"Department has been created")
            return Response(ser.data,status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request,pk=None):
        try:
            if pk is not None:
                company=Departments.objects.get(id=pk)
                ser=DepartmentSerializer(company)
                return Response(ser.data,status=status.HTTP_200_OK)
            all_company=Departments.objects.all()
            ser=DepartmentSerializer(all_company,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        except Company.DoesNotExist:
            print('Departments does not exist')
            return Response('Departments does not exist',status=status.HTTP_404_NOT_FOUND)
        
    
    def put(self,request,pk):
        try:
            company=Departments.objects.get(id=pk)
            ser=DepartmentSerializer(company,data=request.data,partial=True)
            if ser.is_valid():
                ser.save()
                UserLog.objects.create(user=request.user, transactions_reference=f"Department has been updated")
                return Response(ser.data,status=status.HTTP_200_OK)
            return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)
        except Departments.DoesNotExist:
            msg='Departments does not exist'
            print(msg)
            return Response(msg,status=status.HTTP_400_BAD_REQUEST)
        
class DepartmentsDeleteAPI(APIView):    
       def delete(self, request,pk):
        try:
            department=Departments.objects.get(id=pk)
            UserLog.objects.create(user=request.user, transactions_reference=f"Department {department.name} has deleted")
            department.delete()
            return Response({'department has deleted'},status=status.HTTP_200_OK)
        except Departments.DoesNotExist:
            print('Department does not exist')
            return Response('Department does not exist',status=status.HTTP_404_NOT_FOUND)
        
class PasswordReset(APIView):
    authentication_classes = []
    permission_classes = []
    def put(self,request):
        print('data---', request.data)
        serializer = ResetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = CustomUser.objects.get(email=serializer.data.get("email"))
            user.set_password(serializer.data.get("new_password"))
            user.save()
            message = {"Message":"Password Reset Successfully"}
            return Response(message,status=status.HTTP_200_OK)
        
        print("Error",serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
           
class GenerateOTP(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self,request):
        email = request.data['email']
        try:
            user = CustomUser.objects.get(email=email)
            otp = random.randint(100000,999999)
            print("OTP", otp)
            user.otp = otp
            user.save()
            ## send email
            subject='Forgot Password OTP'
            html_message=render_to_string('user_otp_mail.html',{'user':user})
            plain_message =strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            to=[user.email,]
            send_mail(subject,
                        plain_message,
                        from_email, 
                        to, 
                        html_message=html_message)
            return Response({"Message":"OTP send successfully"},status=status.HTTP_200_OK)    
        except Exception as e:
            print('error ...',e)
            return Response({"Message":"Invalid Email"},status=status.HTTP_400_BAD_REQUEST)
        
        
class VerifyOTP(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self,request):
        email = request.data['email']
        otp = int(request.data['otp'])
        print("data",request.data)
        try:
            user = CustomUser.objects.get(email=email)
            if user.otp == otp: 
                return Response({"Message":"OTP verified"},status=status.HTTP_200_OK)  
             
            return Response({"Message":"Invalid OTP"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print("Error",e)
            return Response({"Message":"Invalid Email"},status=status.HTTP_400_BAD_REQUEST)