from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import *

# Create your views here.
def notes_index(request):
    return render(request,'notes_index.html')

@login_required
def notes_list(request):
    return render(request,"notes_list.html")

def notes_create(request):
    return render(request,"notes_list.html")

def notes_edit(request):
    return render(request,"notes_list.html")

def notes_delete(request):
    return render(request,"notes_list.html")

def register(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect("notes_list")
    else:
        form = UserRegistrationForm()
        
    
    return render(request,'registration/register.html',{'form':form})