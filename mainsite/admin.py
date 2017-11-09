# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Post
# Register your models here.

# 增加多列
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug', 'pub_date')


admin.site.register(Post, PostAdmin)
