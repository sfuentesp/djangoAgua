from django.contrib import admin
from .models import Post, Usuario,Voluntario,Responsabilidad
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Post)
admin.site.register(Voluntario)
admin.site.register(Responsabilidad)