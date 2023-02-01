from django.shortcuts import render, redirect
from .models import AllCourses
from django.contrib.auth.models import User, auth


# Create your views here.

def HomePage(request):
    all = AllCourses.objects.all()
    return render(request, 'HomePage.html', {'all': all})


def VideoPage(request):
    return render(request, 'video.html')


def LoginPage(request):
    if request.method == 'POST':
        User_name = request.POST['User_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.create_user(username='User_name', password=password1, email=email)
        user.save()
        print('User Created')
        return redirect('/')
    else:
        return render(request, 'login.html')
