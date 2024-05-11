from django.shortcuts import *
from django.contrib.auth import *
from Branch.models import *

# Create your views here.
def index(request):
  


    return render(request,"index.html")

def student_logout(requst):
    logout(requst)
    return redirect('/Authentication/student_login')
def staff_logout(request):
    logout(request)
    return redirect('/Authentication/staff_login')
def branch_logout(request):
    logout(request)
    return redirect('/Authentication/branch_login')
# Create your views here.
