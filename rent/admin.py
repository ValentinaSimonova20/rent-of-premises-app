from django.contrib import admin

from .models import Applications, Premises, PurposesOfPremises


class PremisesAdmin(admin.ModelAdmin):
    list_display = ('id', 'areaName', 'describe', 'area', 'floor', 'price')
    list_display_links = ('id', 'areaName', 'describe')
    search_fields = ('areaName', 'describe',)


class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'premises', 'additionalInfo', 'created_at')
    list_display_links = ('id', 'client', 'premises')
    search_fields = ('additionalInfo', )


admin.site.register(Applications, ApplicationsAdmin)
admin.site.register(PurposesOfPremises)
admin.site.register(Premises, PremisesAdmin)
