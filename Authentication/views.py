from django.shortcuts import *
from django.contrib.auth import *
from django.contrib import messages
from Accounts.models import *


# Create your views here.

def student_login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        is_Student = True

        

        if MyUser.objects.filter(username = username, is_Student = is_Student).exists():
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('/Student/dashboard')
            else:
                 messages.error(request, "Incorrect Password, please Try Again!")
            
        else :
            messages.error(request, "Username Does not Exist")
            messages.error(request, "Contact to your Class Admin")
            return redirect('/Authentication/student_login/')
    return render(request, 'authentication/student_login.html')



def staff_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        is_staff= True

        

        if MyUser.objects.filter(username = username, is_StaffAdmin= is_staff).exists():
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                request.session['user_pk'] = user.pk
                return redirect('/Staff/dashboard')
            else:
                 messages.error(request, "Incorrect Password, please Try Again!")
            
        else :
            messages.error(request, "Username Does not Exist")
            messages.error(request, "Contact to your System Administrator")
            return redirect('/Authentication/staff_login/')
    return render(request, 'authentication/staff_login.html')



def branch_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        is_BranchAdmin = True

        

        if MyUser.objects.filter(username = username, is_BranchAdmin = is_BranchAdmin).exists():
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                request.session['user_pk'] = user.pk
                return redirect('/Branch/dashboard')
            else:
                 messages.error(request, "Incorrect Password, please Try Again!")
            
        else :
            messages.error(request, "Username Does not Exist")
            messages.error(request, "Contact to your System Administrator")
            return redirect('/Authentication/branch_login/')
    return render(request, 'authentication/branch_login.html')
