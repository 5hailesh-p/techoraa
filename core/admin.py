from django.contrib import admin
from .models import Contact,SiteSettings
# Register your models here.
admin.site.register(Contact)
admin.site.register(SiteSettings)