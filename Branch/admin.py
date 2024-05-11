from django.contrib import admin
from .models import *

# Register your models here.

class Branchs(admin.ModelAdmin):
    list_display = ['branch_name','branch_code','contact_number']

class Grade(admin.ModelAdmin):
    list_display= ['grade','branch_info']

    
    def branch_info(self, obj):
        return f"{obj.branch.branch_name} ({obj.branch.branch_code})  "

    

class Sub(admin.ModelAdmin):
    list_display= ['grades','subject']

    def grades(self, obj):
        return obj.Grades.grade

class Total_marks(admin.ModelAdmin):
    list_display = ['subject','fa1_marks','fa2_marks','sa1_marks','fa3_marks','fa4_marks','sa2_marks'    ]

    def subject(self, obj):
        return obj.Subjects.subject

admin.site.register(Branch,Branchs)
admin.site.register(Grades,Grade)
admin.site.register(Subjects,Sub)
admin.site.register(TotalMarks,Total_marks)