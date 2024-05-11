from django.contrib import admin
from .models import *

class Studentdata(admin.ModelAdmin):
    # pass
    list_display = ['roll_number','grade','sats_number']
class Branchdata(admin.ModelAdmin):
    list_display = ['phone_number', 'branch_code', 'branch_name']

# Register your models here.
admin.site.register(MyUser)
admin.site.register(BranchAdmin ,Branchdata)
admin.site.register(Staff)
admin.site.register(Student,Studentdata)