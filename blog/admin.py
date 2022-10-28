from django.contrib import admin

from blog.models import Post, Restaurant

# Register your models here.

admin.site.register(Post)  # admin 에 등록하고 
admin.site.register(Restaurant)
