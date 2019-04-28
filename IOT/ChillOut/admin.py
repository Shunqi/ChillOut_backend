from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Author, Entry

admin.site.register([Author, Entry])
