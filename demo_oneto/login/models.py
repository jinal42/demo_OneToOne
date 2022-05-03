from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


      # gender=[('male','Male'),('female','Female')]
      # hobby=[('dance','Dance'),('music','Music'),('reading','Reading')]

# Create your models here.
class UserProfile(models.Model):
      user=models.OneToOneField(User, on_delete=models.CASCADE)
      phone=models.CharField(max_length=10,blank=True)
      # gender=models.CharField(max_length=15,default='female',choices=gender)
     
      gender=models.CharField(max_length=15,default='female')

      #hobby=models.CharField(max_length=255,default='dance',choices=hobby)
      
      hobby=models.CharField(max_length=255,default='dance')



      birth_date = models.DateField(null=True, blank=True)

def __str__(self):  
        return self.user.username

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userprofile.save()