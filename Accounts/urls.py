from django.urls import path
from .views import *

urlpatterns =[
    path('signup_student/', signup_student, name='signup_student'),
    path('signup_staff/', signup_staff, name='signup_staff'),
    path('signup_branch/', signup_branch, name='signup_branch'),
] 