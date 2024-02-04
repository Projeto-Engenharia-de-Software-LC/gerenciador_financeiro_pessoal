from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from gastos.models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'password', 'telefone', 'is_active', 'is_staff', 'is_superuser')

admin.site.register(CustomUser,CustomUserAdmin)
# Register your models here.
