from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Gasto, Usuario, Receita

admin.site.register(Gasto)
admin.site.register(Receita)
admin.site.register(Usuario)