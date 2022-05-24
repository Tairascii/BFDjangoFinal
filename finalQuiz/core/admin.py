from django.contrib import admin

# Register your models here.

from core.models import Book, Journal, UserProf

admin.site.register(Book)
admin.site.register(Journal)
admin.site.register(UserProf)
