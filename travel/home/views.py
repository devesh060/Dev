# from os import login_tty
from math import ceil
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import ImageForm
from .models import Image

from home.models import Contact
# Create your views here.


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/home")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, "login.html")


def index(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")


def about(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request, 'About.html')


def Services(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request, 'Services.html')


def contact(request):
    if request.user.is_anonymous:
        return redirect("/")
    if request.method == "POST":
        username = request.POST.get('username')
        First_name = request.POST.get('First_name')
        Last_name = request.POST.get('Last_name')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(username=username, First_name=First_name, Last_name=Last_name,
                          city=city, state=state, zip=zip, email=email, desc=desc)
        contact.save()
    return render(request, 'contact.html')


def Course(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request, 'Course.html')


# def upload(request):
#     tex = tecRec_data.objects.all()
#     tec = {"name": tex}
#     return render(request, 'upload.html', tec)


def Dbms(request):
    if request.user.is_anonymous:
        return redirect("/")
    return render(request, 'Dbms.html')


def texRec(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()

    return render(request, 'texRec.html',{'img': img, 'form': form})


def logoutUser(request):
    logout(request)
    return redirect("/")
