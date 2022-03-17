from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
def home(request):
    return render(request, 'form/index.html' )

def signin(request):
    return render(request, 'form/signin.html')

def signup(request):
    if request == "POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        repassword=request.POST['rpassword']

        user=User.objects.create_user(username,email,password)
        user.save()

        messages.success(request,"Your account has been created")
        return redirect('signin')




    return render(request, 'form/signup.html')

def signout(request):
    return render(request, 'form/signout.html')
