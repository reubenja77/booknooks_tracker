from django.contrib import admin

from .models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date_read", "owner")
    search_fields = ("title", "author", "owner__username")
    list_filter = ("date_read",)
