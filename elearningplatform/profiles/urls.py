from django.urls import path
from .views import ProfilesListView, ProfileDetailView, ProfileStudentUpdate


urlpatterns = [
    path('', ProfilesListView.as_view(), name="profiles"),
    path('<int:id>/', ProfileDetailView.as_view(), name="profiles"),
    path('student/<int:id>/', ProfileStudentUpdate.as_view(), name="student-update"),
]
