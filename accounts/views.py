from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import EmpForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def landpage(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('prof')
    return render(request,'index.html')
# Create your views here.

def register(request):
    form=EmpForm()
    context={'regform':form}
    if request.method=='POST':
        regform=EmpForm(request.POST)
        if regform.is_valid():
            regform.save()
            return redirect('home')
    return render(request,'reg.html',context)

@login_required(login_url='home')
def profile(request):
    return render(request,'profile.html')

def logoutpage(request):
    logout(request)
    return redirect('home')