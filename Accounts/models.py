from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    is_Student = models.BooleanField(default=False)
    is_StaffAdmin = models.BooleanField(default=False)
    is_BranchAdmin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Student(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    SOCIAL_CATEGORY_CHOICES = [
        ('General', 'General'),
        ('OBC', 'Other Backward Class'),
        ('SC', 'Scheduled Caste'),
        ('ST', 'Scheduled Tribe'),
        ('EWS', 'Economically Weaker Section'),
        # Add more options as needed
    ]
    DISABILITY_CHOICES = [
        ('None', 'None'),
        ('Visual', 'Visual Impairment'),
        ('Hearing', 'Hearing Impairment'),
        ('Mobility', 'Mobility Impairment'),
        ('Cognitive', 'Cognitive Impairment'),
        ('Other', 'Other'),
        # Add more options as needed
    ]
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        # Add more options as needed
    ]
    GRADE_CHOICES = [
        ('lkg', 'LKG'),
        ('ukg', 'UKG'),
        ('1', 'Grade 1'),
        ('2', 'Grade 2'),
        ('3', 'Grade 3'),
        ('4', 'Grade 4'),
        ('5', 'Grade 5'),
        ('6', 'Grade 6'),
        ('7', 'Grade 7'),
        ('8', 'Grade 8'),
        ('9', 'Grade 9'),
        ('10', 'Grade 10'),
    ]
    
    # Add additional fields specific to students
    image = models.ImageField(upload_to='static/Student/images/', blank=True, null=True)
    roll_number = models.CharField(max_length=15)
    sats_number = models.CharField(max_length=10,unique=True)
    grade = models.CharField(max_length=100 ,choices=GRADE_CHOICES)
    
    phone_number = models.CharField(max_length=15)  # You might want to use PhoneNumberField if you're using a library like Django Phonenumber Field
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    fatherName = models.CharField(max_length=100)
    motherName = models.CharField(max_length=100)
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob = models.DateField(blank=True, null=True)
    aadharNumber =  models.CharField(max_length=12, unique=True, null=True,blank=True)
    religion = models.CharField(max_length=15, null=True,blank=True)
    Social_catagory = models.CharField(max_length=50, choices=SOCIAL_CATEGORY_CHOICES)
    medium = models.CharField(max_length=10)
    disablity = models.CharField(max_length=20, choices=DISABILITY_CHOICES, default='None')
    blood_group =  models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES,null=True, blank=True) 


        
    # Address 
    
    address = models.CharField(max_length=100, null=True,blank=True)
    city = models.CharField(max_length=100, null=True,blank=True)
    state = models.CharField(max_length=100, null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)
    
    # Contact details
    parent_contact  =  models.CharField(max_length=15, null=True,blank=True)
    student_contact  =  models.CharField(max_length=15, null=True, blank=True)
    parent_email = models.EmailField(null=True, blank=True)
    student_email = models.EmailField(null=True, blank=True)
    
    #  school code
    branch_code = models.IntegerField(null=True,blank=True)
    branch_name = models.CharField(max_length=100, null=True,blank=True)
    
    #student transfer
    tc_issued= models.BooleanField(default=False) 
    tc= models.CharField(max_length=20, null=True,blank=True)

class Staff(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)
    # Add additional fields specific to staff
    aadharNumber =  models.CharField(max_length=12, unique=True)
    branch_code = models.IntegerField()
    roll_for = models.CharField(max_length=100)
    assigned_class = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    joining_date = models.DateField()
    phone_number = models.CharField(max_length=15)  # Or use PhoneNumberField from django-phonenumber-field
    address = models.TextField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=(('male', 'Male'), ('female', 'Female'), ('other', 'Other')))
    marital_status = models.CharField(max_length=20, choices=(('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed')))
    qualification = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_number = models.CharField(max_length=15)
    emergency_contact_relationship = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/Staff/images/', blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    qualification_certificate = models.FileField(upload_to='Staff/qualification_certificates/', blank=True, null=True)
    languages_known = models.CharField(max_length=255)
    


class BranchAdmin(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, primary_key=True)

    # Add additional fields specific to branch admin
    branch_code = models.IntegerField()
    branch_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=(('male', 'Male'), ('female', 'Female'), ('other', 'Other')))
    date_of_birth = models.DateField()
    languages_known = models.CharField(max_length=255)
    phone_number =models.CharField(max_length=15,null=True,blank=True)
    image = models.ImageField(upload_to='static/Branch/images/', blank=True, null=True)
  