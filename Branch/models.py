from django.db import models
from Accounts.models import *

# Create your models here.


class Branch(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING,null=True)
    branch_name = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    pincode = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)
    def __str__(self):
        return self.branch_code
   

class Grades(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    grade  = models.CharField(max_length=10)
    def __str__(self):
        return self.grade
    
class Subjects(models.Model):
    grades = models.ForeignKey(Grades, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    def __str__(self):
        return self.subject
    
class TotalMarks(models.Model):
    Subjects = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    fa1_marks = models.CharField(max_length=10,null=True,blank=True)
    fa2_marks = models.CharField(max_length=10,null=True,blank=True)
    fa3_marks = models.CharField(max_length=10,null=True,blank=True)
    fa4_marks = models.CharField(max_length=10,null=True,blank=True)
    sa1_marks = models.CharField(max_length=10,null=True,blank=True)
    sa2_marks = models.CharField(max_length=10,null=True,blank=True)
