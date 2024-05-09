from datetime import timezone
from django.shortcuts import *
from .models import *
from Student.models import *
from Staff.models import *
from django.contrib import messages
from django.contrib.auth import *
from django.core.files.uploadedfile import InMemoryUploadedFile







# # Create your views here.
# def student_register(request):
#     if request.method == 'POST':
#         first_name = request.POST['firstName']
#         last_name = request.POST['lastName']
#         username = request.POST['userName']
#         password = request.POST['password']
#         user = Student.objects.create(
#             first_name = first_name,
#             last_name = last_name,
#             username = username,
#             )
#         user.set_password(password)
#         user.save() 
#         return redirect('/Authentication/student_login')
#     return render(request, 'authentication/student/student_register.html')


# def staff_register(request):
   
#     if request.method == 'POST':
#         first_name = request.POST['firstName']
#         last_name = request.POST['lastName']
#         username = request.POST['userName']
#         password = request.POST['password']
#         user = Staff.objects.create(
#             first_name = first_name,
#             last_name = last_name,
#             username = username,
#             )
#         user.set_password(password)
#         user.save() 
#         return redirect('/Authentication/staff_login/ ')
#     return render(request, "authentication/staff/staff_register.html")

# # Create your views here.
# def generate_roll_number(student):
#     # Extract the last two digits of the current year
#     current_year_last_two_digits = timezone.now().year % 100
    
#     # Extract the last two digits of the student's admission year
#     admission_year_last_two_digits = int(str(student.date_joined.year)[-2:])
    
#     # Format the roll number as YYClassOrderNumber
#     roll_number = "{:02d}{}{:02d}-{}".format(admission_year_last_two_digits, student.grade[:2].upper(), student.id % 100, student.first_name[0].upper())
    
#     return roll_number


# def branch_register(request):
#     if request.method == "POST":
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         password = request.POST['password']
#         email = request.POST['email']
#         phone_number = request.POST['phone_number']
#         branch_code = request.POST['branch_code']
#         branch_name = request.POST['branch_name']
#         gender = request.POST['gender']
#         date_of_birth = request.POST['date_of_birth']
#         languages_known = request.POST['languages_known']
#         image = request.FILES.get('image')
#         required_fields = ['first_name', 'last_name', 'username', 'password', 'email', 'phone_number', 'branch_code',
#                    'branch_name', 'gender', 'date_of_birth', 'languages_known', 'image']
#         for field_name in required_fields:
#             if not locals().get(field_name):
#                 raise ValueError(f"Field '{field_name}' is missing from the request.")

# # Create BranchAdmin object
#         branch = BranchAdmin.objects.create(
#             first_name= first_name,
#             last_name=last_name,
#             username=username,
#             email=email,
#             branch_code=branch_code,
#             branch_name=branch_name,
#             gender=gender,
#             date_of_birth=date_of_birth,
#             languages_known=languages_known,
#             image=image,
#             phone_number=phone_number
#         )

#     # Set password for the user
#         branch.set_password(password)
#         branch.save()

#     # Optionally, you can handle the phone_number field separately, as it's not included in the default User model
        

#         return redirect('/Authentication/branch_login')
#     return render(request, 'authentication/branch/branch_register.html')



# def branch_dashboard(request):
#     user_pk = request.session.get('user_pk')
#     userlist = user_pk - 1
#     print("session code is :",userlist)
#     Branch = BranchAdmin.objects.all()[userlist]
#     context = {'user': Branch}
#     return render (request, 'branch/dashboard.html',context )