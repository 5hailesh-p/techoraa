from django.contrib import admin
from .models import Contact,SiteSettings,Contact_form
# Register your models here.
admin.site.register(Contact_form)
admin.site.register(Contact)
admin.site.register(SiteSettings)

class SiteSettingsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()