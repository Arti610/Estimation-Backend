from django.db import models
from .managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
import datetime
from rest_framework.authtoken.models import Token
from django.conf import settings

class Departments(models.Model):
    name=models.CharField(max_length=225,null=True,blank=True)
    description=models.TextField(blank=True,null=True)
    created_by = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Updated Date")

    def __str__(self):
        return str(self.name)
    
USER_TYPES = (
    ("Admin", "Admin"),
    ("Operator", "Operator"),
    ("Customer", "Customer"),
)
ACC_STATUS=(
    ('Active', 'Active'),
    ('Closed', 'Closed'),
    ('Suspended','Suspended'),
)
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(null=True, unique=True)
    first_name = models.CharField(max_length=50,null=True, verbose_name="First Name ")
    last_name = models.CharField(max_length=50, null=True, verbose_name="Last Name ")
    date_joined = models.DateTimeField(default=datetime.datetime.now)
    phone_number = models.PositiveBigIntegerField(null=True, blank=True, verbose_name="Phone Number ", help_text="Optional")
    address = models.CharField(max_length=150,null=True, blank=True, verbose_name="Address")
    profile_image = models.FileField(default="",upload_to="profile image",null=True,blank=True, verbose_name="Profile Image")
    user_type = models.CharField(max_length=30, choices=USER_TYPES, null=True,blank=True)
    account_status=models.CharField(max_length=30, choices=ACC_STATUS, null=True,blank=True,default='Active')
    last_login=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    department=models.ForeignKey(Departments,models.SET_NULL,null=True,blank=True)
    otp=models.IntegerField(null=True,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "All Users"
        verbose_name_plural = "All Users"

    def __str__(self):
        return f"{self.email}"
    
    
class MultiToken(Token):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='auth_token',
            on_delete=models.CASCADE, verbose_name=_("User"))
    

class Company(models.Model):
    company_name=models.CharField(max_length=225,null=True,blank=True)
    address=models.CharField(max_length=255,null=True,blank=True)
    city=models.CharField(max_length=255,null=True,blank=True)
    state=models.CharField(max_length=255,null=True,blank=True)
    zip=models.CharField(max_length=255,null=True,blank=True)
    country=models.CharField(max_length=255,null=True,blank=True)
    tax_id=models.CharField(max_length=255,null=True,blank=True)
    currency=models.CharField(max_length=255,null=True,blank=True)
    phone=models.CharField(max_length=255,null=True,blank=True)
    mobile=models.CharField(max_length=255,null=True,blank=True)
    email=models.EmailField(unique=True,blank=True,null=True)
    website=models.CharField(max_length=255,null=True,blank=True)
    company_logo=models.ImageField(upload_to='company_logo',null=True,blank=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Created Date")
    updated_date = models.DateTimeField(auto_now=True, null=True, verbose_name="Updated Date")
    
    def __str__(self):
        return f"{self.company_name}"

    