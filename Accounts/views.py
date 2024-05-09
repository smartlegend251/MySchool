from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def signup_student(request):
    if request.method == 'POST':
        # Extract data from the request
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check if passwords match
        if password1 != password2:
            return render(request, 'signup_student.html', {'error': "Passwords don't match"})

        # Create user
        user = MyUser.objects.create_user(username=username, email=email, password=password1)
        user.first_name = first_name
        user.last_name = last_name
        user.is_Student = True
        user.save()

        # Create student
        student = Student.objects.create(
            user=user,
            # Add other student-related data here
            image=request.FILES.get('image'),
            roll_number=request.POST.get('roll_number'),
            sats_number=request.POST.get('sats_number'),
            grade=request.POST.get('grade'),
            phone_number=request.POST.get('phone_number'),
            middle_name=request.POST.get('middle_name'),
            fatherName=request.POST.get('fatherName'),
            motherName=request.POST.get('motherName'), 
            gender=request.POST.get('gender'),
            dob=request.POST.get('dob'),
            # aadharNumber=request.POST.get('aadharNumber'),
            # religion=request.POST.get('religion'),
            # Social_catagory=request.POST.get('Social_catagory'),
            medium=request.POST.get('medium'),
            disablity=request.POST.get('disablity'),
            # blood_group=request.POST.get('blood_group'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            pincode=request.POST.get('pincode'),
            parent_contact=request.POST.get('parent_contact'),
            # student_contact=request.POST.get('student_contact'),
            # parent_email=request.POST.get('parent_email'),
            # student_email=request.POST.get('student_email'),
            branch_code=request.POST.get('branch_code'),
            branch_name=request.POST.get('branch_name'),
            # tc_issued=False,
            # tc=request.POST.get('tc'),

        )
        student.save()
        return redirect('/Authentication/student_login/') 
    return render(request, 'accounts/student_register.html')


def signup_staff(request):
    if request.method == 'POST':
        # Extract data from the request
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check if passwords match
        if password1 != password2:
            return render(request, 'signup_student.html', {'error': "Passwords don't match"})

        # Create user
        user = MyUser.objects.create_user(username=username, email=email, password=password1)
        user.first_name = first_name
        user.last_name = last_name
        user.is_StaffAdmin = True
        user.save()

        # Create student
        staff = Staff.objects.create(
            user=user,
            # Add other student-related data here
            # aadharNumber=request.POST.get('aadharNumber'),
            branch_code=request.POST.get('branch_code'),
            roll_for=request.POST.get('roll_for'),
            assigned_class=request.POST.get('assigned_class'),
            branch_name=request.POST.get('branch_name'),
            position=request.POST.get('position'),
            joining_date=request.POST.get('joining_date'),
            phone_number=request.POST.get('phone_number'),
            address=request.POST.get('address'),
            date_of_birth=request.POST.get('date_of_birth'),
            gender=request.POST.get('gender'),
            # marital_status=request.POST.get('marital_status'),
            qualification=request.POST.get('qualification'),
            experience_years=request.POST.get('experience_years'),
            # emergency_contact_name=request.POST.get('emergency_contact_name'),
            # emergency_contact_number=request.POST.get('emergency_contact_number'),
            # emergency_contact_relationship=request.POST.get('emergency_contact_relationship'),
            image=request.FILES.get('image'),
            # salary=request.POST.get('salary'),
            qualification_certificate=request.FILES.get('qualification_certificate'),
            languages_known=request.POST.get('languages_known'),
                    
        )
        staff.save()
        return redirect('/Authentication/staff_login/')
    return render(request, 'accounts/staff_register.html')


def signup_branch(request):
    if request.method == 'POST':
        # Extract data from the request
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check if passwords match
        if password1 != password2:
            return redirect('/Authentication/branch_login/', {'error': "Passwords don't match, Please Retry"})
    
        # Create user
        user = MyUser.objects.create_user(username=username, email=email, password=password1)
        user.first_name = first_name
        user.last_name = last_name
        user.is_BranchAdmin = True
        user.save()

        # Create student
        branch = BranchAdmin.objects.create(
            user=user,
            # Add other student-related data here
            branch_code=request.POST.get('branch_code'),
            branch_name=request.POST.get('branch_name'),
            gender=request.POST.get('gender'),
            date_of_birth=request.POST.get('date_of_birth'),
            languages_known=request.POST.get('languages_known'),
            phone_number=request.POST.get('phone_number'),
            image=request.FILES.get('image'),
        )
        branch.save()
        return redirect('/Authentication/branch_login/')
    return render(request, 'accounts/branch_register.html')