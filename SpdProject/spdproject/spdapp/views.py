from  django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render

from .forms import RegistrationForm
from .models import Registration


def indexfunction(request):
    return render(request,"index.html")
def registration(request):
    form = RegistrationForm()

    if request.method == "POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Successfully Registered"
            return render(request,"regsuccess.html",{"msg":msg})
        else:
            return HttpResponse("Registration Failed")

    return render(request,"registration.html",{"form":form})
def userlogin(request):
    return render(request,"userlogin.html")

def checkuserlogin(request):
    emailid=request.POST["emailid"]
    pwd=request.POST["password"]

    flag=Registration.objects.filter( Q(email=emailid) & Q(password=pwd) )

    if flag:
        return render(request,"userhome.html")
    else:
        msg="Login Failed"
        return render(request, "userlogin.html",{"msg":msg})

def userhome(request):
    return render(request,"userhome.html")

def userlogout(request):
    return render(request,"userlogin.html")
def newproject(request):
    return render(request,"zodiacsign.html")

def checksign(request):
    return render(request,"checksign.html")

def create_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_list')  # Redirect to the list of registrations
    else:
        form = RegistrationForm()
    return render(request, 'create_registration.html', {'form': form})

def registration_list(request):
    registrations = Registration.objects.all()
    return render(request, 'registration_list.html', {'registrations': registrations})

def update_registration(request, pk):
    registration = Registration.objects.get(pk=pk)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            form.save()
            return redirect('registration_list')  # Redirect to the list of registrations
    else:
        form = RegistrationForm(instance=registration)
    return render(request, 'update_registration.html', {'form': form})

def delete_registration(request, pk):
    registration = Registration.objects.get(pk=pk)
    if request.method == 'POST':
        registration.delete()
        return redirect('registration_list')  # Redirect to the list of registrations
    return render(request, 'delete_registration.html', {'registration': registration})

