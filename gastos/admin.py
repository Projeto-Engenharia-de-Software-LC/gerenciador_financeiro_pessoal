from django.contrib import admin
from .models import Gasto, CustomUser, Receita

admin.site.register(Gasto)
#admin.site.register(CustomUser)
admin.site.register(Receita)
