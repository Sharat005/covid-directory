from django.contrib import admin
from .models import PatientInfo
from screen.admin import ScreenInline

admin.site.site_header = "BCC Covid-Directory"
admin.site.site_title = "Covid-Directory"
admin.site.index_title = "Welcome to CovidDirectory Admin Panel"

# Register your models here.
@admin.register(PatientInfo)
class PatientInfoAdmin(admin.ModelAdmin):
    # inlines = [ScreenInline]
    pass
