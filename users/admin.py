from django.contrib import admin
from .models import ProfileModel
# Register your models here.
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'image']
admin.site.register(ProfileModel, ProfileModelAdmin)
