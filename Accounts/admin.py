from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(MyUser)
admin.site.register(BranchAdmin)
admin.site.register(Staff)
admin.site.register(Student)