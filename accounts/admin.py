from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import*


class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email" , "profile_image", "first_name","last_name", "phone_number", "address","is_active", "date_joined",'department' ] 
    search_fields = ["email", "first_name", "last_name", "phone_number",]
   
    fieldsets = (
        ('User Details', {'fields': ('email','password')}),
        ('Personal Details', {'fields': ('first_name', 'last_name', 'profile_image', 'phone_number','department')}),
        ('Permission Info', {
            'classes': ('wide',),
            'fields': ('is_staff', 'is_active', 'is_superuser','groups', 'user_permissions', 'date_joined',)}
        )
    )
    
    add_fieldsets = (
        ('Personal Info', {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'profile_image', 'phone_number', 'password1', 'password2')}
        ),
    )
    ordering = ('email',)
    filter_horizontal = ['groups', 'user_permissions']
    

admin.site.unregister(Group)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(MultiToken)
admin.site.register(Departments)
admin.site.register(Company)