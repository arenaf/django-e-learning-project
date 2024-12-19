from django.urls import path
from .views import TeacherView, StudentView, ProfileUpdate

urlpatterns = [
    path('teacher_signup/', TeacherView, name="teacher_signup"),
    path('student_signup/', StudentView, name="student_signup"),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
]
