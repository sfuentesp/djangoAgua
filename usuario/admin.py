from django.contrib import admin
from .models import Post, Usuario
# Register your models here.

admin.site.register(Usuario)

admin.site.register(Post)