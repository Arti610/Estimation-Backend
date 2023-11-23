from .views import *
from django.urls import path

urlpatterns = [
    path('api/createuser',UserRegistration.as_view()),
    path('api/userlist',CustomUserList.as_view()),
    path('api/user/<int:id>',GetCustomUser.as_view()),
    path('api/user/login',UserLogin.as_view()),
    path('api/updateuser/<int:id>',UpdateUserProfile.as_view()),
    path("api/user/logout", UserLogout.as_view()),
    path("api/user/change_password",ChangePassword.as_view()),
    path("api/user/delete/<int:pk>",UserDelete.as_view()),
    
    #  company
    path("api/company",CompanyAPI.as_view()),
    path("api/company/<int:pk>",CompanyAPI.as_view()),
    
    #  Department
    path("api/department",DepartmentsAPI.as_view()),
    path("api/department/<int:pk>",DepartmentsAPI.as_view()),
    path("api/delete_department/<int:pk>",DepartmentsDeleteAPI.as_view()),
    
    
    path('api/generate_otp',GenerateOTP.as_view(), name='generate_otp'),
    path('api/verify_otp',VerifyOTP.as_view(), name='verify_otp'),
    path('api/password_reset',PasswordReset.as_view(), name='password_reset'),


]