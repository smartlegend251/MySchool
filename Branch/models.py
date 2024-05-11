from django.db import models

# Create your models here.
class Branch(models.Model):
    branch_name = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    pincode = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)


class Grades(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    grade  = models.CharField(max_length=10)

class Subjects(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)