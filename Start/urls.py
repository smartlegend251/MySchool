
from django.urls import path
from .views import *
from Authentication.views import *

urlpatterns = [
path('', index, name='index'),
path('student_logout/', student_logout, name='student_logout'),
path('staff_logout/', staff_logout, name='staff_logout'),
path('branch_logout/', branch_logout, name='branch_logout'),
]
