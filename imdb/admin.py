from django.contrib import admin
from .models import Actor, Movie, Role
# Register your models here.

admin.site.register([Actor, Movie, Role])
