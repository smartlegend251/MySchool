from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse
from Accounts.models import *

# Create your views here.

# # login for student
# @login_required(login_url=settings.STUDENT_LOGIN_URL)

def student_dashboard(request):
    user = request.user
    print('the output is : ', user)

    try:
        student = Student.objects.get(user=user)
        # print('the output is : ', branch)
        image = student.image
        print('the output is : ', image)
    except Student.DoesNotExist:
        # Handle the case where the BranchAdmin instance doesn't exist for the user
        image = None
    return render(request, 'student/dashboard.html',{'image':image})


def student_attendance(request):
   

    # Retrieve attendance data from the database
    # Assuming Attendance model has 'student' (ForeignKey to User model), 'date' (DateField), and 'present' (BooleanField)
    # attendance_data = Attendance.objects.all()
    
    # Calculate total days and present days
    # total_days = len(attendance_data)
    # present_days = sum(1 for attendance in attendance_data if attendance.present)
    
    # Calculate attendance percentage
    # attendance_percentage = (present_days / total_days) * 100 if total_days > 0 else 0
    
    
    return render(request, 'student/attendance.html')















def student_score(request):
    class_name = "Class X" 
    marks_data = {
        '1st Language': {'FA1': 85, 'FA2': 80, 'SA1': 90, 'FA3': 85, 'FA4': 80, 'SA2': 90},
        '2nd Language': {'FA1': 75, 'FA2': 70, 'SA1': 85, 'FA3': 75, 'FA4': 70, 'SA2': 85},
        '3rd Language': {'FA1': 80, 'FA2': 75, 'SA1': 88, 'FA3': 80, 'FA4': 75, 'SA2': 88},
        'Maths': {'FA1': 90, 'FA2': 85, 'SA1': 95, 'FA3': 90, 'FA4': 85, 'SA2': 95},
        'Science': {'FA1': 85, 'FA2': 80, 'SA1': 90, 'FA3': 85, 'FA4': 80, 'SA2': 90},
        'Social Studies': {'FA1': 90, 'FA2': 85, 'SA1': 95, 'FA3': 90, 'FA4': 85, 'SA2': 95},
    }
    
    context = {
        'class_name': class_name,   
        'marks_data': marks_data
    }
    return render (request , 'student/score.html',context)

def student_notification(request):
    return render (request, 'student/notification.html')

def student_profile(request):
    return render (request, 'student/profile.html')



# Create your views here.
