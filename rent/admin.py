from django.contrib import admin

from .models import User, Applications, Premises

admin.site.register((User, Applications, Premises))
