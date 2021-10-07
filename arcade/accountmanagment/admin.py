from django.contrib import admin
from .models import User
# Register your models here.

#adding custom user to admin-panel
admin.site.register(User)