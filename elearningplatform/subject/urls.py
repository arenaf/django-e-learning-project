from django.urls import path
from .views import SubjectView, SubjectListView, SubjectDetailView, FileView, FileDetailView, FileDeleteView, SubjectDeleteView


urlpatterns = [
    path('', SubjectListView.as_view(), name="subject"),
    path('<int:pk>/', SubjectDetailView.as_view(), name="subject"),
    path('new-subject', SubjectView.as_view(), name="new-subject"),
    path('delete-subject/<int:pk>', SubjectDeleteView.as_view(), name="delete-subject"),
    path('new-file/<int:id>', FileView, name="new-file"),
    path('file/<int:pk>', FileDetailView.as_view(), name="file"),
    path('delete-file/<int:pk>', FileDeleteView.as_view(), name="delete-file"),
]