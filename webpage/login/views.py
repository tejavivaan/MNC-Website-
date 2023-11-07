from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect,render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'login/index.html')
def sinup(request):

     if request.method == 'POST':
         username = request.POST.get('username')
         fname = request.POST.get('fname')
         lname = request.POST.get('lname')
         email = request.POST.get('email')
         pass1 = request.POST.get('pass1')
         pass2 = request.POST.get('pass2')

         my_user = User.objects.create_user(username,email,pass1)
         my_user.first_name = fname
         my_user.last_name = lname

         my_user.save()

         messages.success(request,"Your Account is Created Successfully.")

         return redirect('sinin')


     return render(request,'login/sinup.html')
def sinin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,"login/index.html",{'fname':fname})
        else:
            messages.error(request,"Bad Credentials")
            return redirect('index')


    return render(request,'login/sinin.html')

def aboutus(request):
    return render(request,'about.html')

def contactus(request):
    return render(request,'contactus.html')

def logout_user(request):
    logout(request)
    return redirect('index')

def profile(request):
    context = {
        'user': request.user
    }
    return render(request,'profile.html',context)