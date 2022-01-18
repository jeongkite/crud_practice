from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Category)


@admin.register(Mark)
class MarkAdmim(admin.ModelAdmin):
    list_display = ['name', 'url', 'category']
    list_display_links = ['name', 'category']
    search_fields = ['name', 'category__name']
