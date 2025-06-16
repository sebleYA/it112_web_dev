from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'year_published')  # shown in the list view
    search_fields = ('title', 'author')                   # enables search box
    list_filter = ('year_published',)                     # adds sidebar filter