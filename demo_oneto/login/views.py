import django
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login 

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
              print("🚀 ~ file: views.py ~ line 14 ~ phone", phone)
              print("🚀 ~ file: views.py ~ line 15 ~ gender", gender)
              print("🚀 ~ file: views.py ~ line 16 ~ hobby", hobby)
              print("🚀 ~ file: views.py ~ line 17 ~ birth_date", birth_date)
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

def login_view(request):
      if request.method=="POST":
            uname=request.POST['user_name']
            upwd=request.POST['password']
            
            print("-------------------",uname)
            print("-------------------",upwd)



            user=authenticate(username=uname,password=upwd)
            if user is not None:
                  login(request,user)
                  return render(request,'login/profile.html',{'uname':user})
            else:
                  HttpResponse("somthing wrong...")
                  return HttpResponseRedirect('/login/')
     
      # print('login......')
      return render(request,'login/login.html')


def profile(request):
       return render(request,'login/profile.html')