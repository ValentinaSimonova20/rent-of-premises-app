from django.contrib import admin

from .models import Applications, Premises

admin.site.register((Applications, Premises))
