from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login, logout
from .models import Customer
#sinup view
def signup(request):
    if request.method == "POST":
        rs= SignUpForm(request.POST)
        if rs.is_valid():
            messages.success(request, "Account created successfully!!")
            rs.save()
    else:
        rs= SignUpForm()
    return render(request, 'custinfo/signup.html', {'form':rs})
# Create your views here.
# login view
def clogin(request):
    if request.method=="POST":
        lg=AuthenticationForm(request=request, data=request.POST)
        if lg.is_valid():
            uname=lg.cleaned_data['username']
            upass=lg.cleaned_data['password']
            user= authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/cf/cprofile/')
    else:
        lg=AuthenticationForm()
    return render(request, 'custinfo/clogin.html', {'form':lg})

#Customer profile
def cprofile(request):
    if request.method=="GET":
        pro=Customer.objects.all()
    return render(request, 'custinfo/profile.html', {'name':request.user})

#Customer logout
def clogout(request):
    logout(request)
    return HttpResponseRedirect('/cf/clogin/')



