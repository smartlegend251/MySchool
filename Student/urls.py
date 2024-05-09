
from django.urls import path
from .views import *

urlpatterns = [
path('dashboard', student_dashboard, name='student_dashboard' ),
path('attendance/', student_attendance, name='student_attendance'),
path('score/', student_score, name='student_score'),
path('notification/', student_notification, name='student_notification'),
path('profile/', student_profile, name='student_profile'),
]
