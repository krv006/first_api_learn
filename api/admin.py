from django.contrib import admin
from .models import Author, Book, Publisher, Magazine
# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Magazine)