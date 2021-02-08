from django.contrib import admin

# Register your models here.
from .models import Serial, Cast

admin.site.register(Serial)
admin.site.register(Cast)