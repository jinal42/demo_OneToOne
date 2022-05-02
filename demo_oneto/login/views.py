import django
from django.shortcuts import redirect, render

from .models import UserProfile
from .forms import UserForm,ProfileForm


# Create your views here.
def user_profile(request):
      user_form = UserForm(request.POST)
      if user_form.is_valid():
        user = user_form.save()

        if request.method == "POST":
              phone = request.POST.get("phone")
              gender = request.POST.get("gender")
              # hobby=request.POST["hobby"]
              hobby=request.POST.getlist('hobby[]')

              x =','.join(hobby)
              hobby=str(x)

              birth_date=request.POST.get("birth_date")
              # print("🚀 ~ file: views.py ~ line 14 ~ phone", phone)
              # print("🚀 ~ file: views.py ~ line 15 ~ gender", gender)
              # print("🚀 ~ file: views.py ~ line 16 ~ hobby", hobby)
              # print("🚀 ~ file: views.py ~ line 17 ~ birth_date", birth_date)
              profile = UserProfile(phone=phone,gender=gender,hobby=hobby,birth_date=birth_date)
              profile.user = user
                
              
              profile.save()


      profile_form = ProfileForm(request.POST)
           
      if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = UserProfile(phone=phone,gender=gender,hobby=hobby,birth_date=birth_date)
            print("====================================",profile)
            profile.user = user
            profile.save()
            return render(request,'login/reg.html',{'user_form': user_form,'profile_form': profile_form})

      else:
        user_form = UserForm()
        profile_form = ProfileForm()
      return render(request,'login/reg.html',{'user_form': user_form,'profile_form': profile_form})