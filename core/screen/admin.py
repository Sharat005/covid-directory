from django.contrib import admin
from .models import Screen

# Register your models here.
class ScreenInline(admin.TabularInline):
    model = Screen
    extra = 0

admin.site.register(Screen)