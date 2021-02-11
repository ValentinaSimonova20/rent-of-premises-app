from django.contrib import admin

from .models import Applications, Premises, PurposesOfPremises

admin.site.register((Applications, Premises, PurposesOfPremises))
