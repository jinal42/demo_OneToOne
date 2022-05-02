from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import  UserProfile,User

# Register your models here.


@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
 list_display=('id','user','phone','gender','hobby','birth_date')

