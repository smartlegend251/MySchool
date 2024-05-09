
from django.urls import path
from .views import *

urlpatterns = [
# path('student_application', student_register, name='studentregister' ),
# path('staff_application', staff_register, name='staffregister' ),
# path('branch_register',branch_register, name='branchRegister'),
path('dashboard',branch_dashboard, name='branch_dashboard'),



]
