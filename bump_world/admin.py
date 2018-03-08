# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
	list_display=['title','created_time','modified_time','catagory','author']

admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)


























































