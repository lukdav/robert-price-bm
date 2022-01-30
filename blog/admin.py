from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('date_posted', 'title')
    search_fields = ['title', 'article']


admin.site.register(Blog, BlogAdmin)
