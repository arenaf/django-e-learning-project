from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile
from registration.forms import StudentForm


# Create your views here.
class ProfilesListView(ListView):
    model = Profile
    template_name = "profiles/profile_list.html"
    paginate_by = 20


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profiles/profile_detail.html"

    def get_object(self):
        return get_object_or_404(Profile, user__id=self.kwargs['id'])


class ProfileStudentUpdate(UpdateView):
    form_class = StudentForm
    template_name = 'profiles/profile_student_update.html'
    success_url = reverse_lazy('profiles')

    # Get the student profile
    def get_object(self):
        return get_object_or_404(Profile, user__id=self.kwargs['id'])
