from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .forms import TeacherForm, StudentForm, UserForm
from .models import Profile
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
# Import access decorators
from subject.views import teacher_access, TeacherRequiredMixin


# Create your views here.

@login_required
@user_passes_test(teacher_access)
def TeacherView(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        teacher_form = TeacherForm(request.POST)

        if user_form.is_valid() and teacher_form.is_valid():
            user = user_form.save()
            user.save()
            teacher = teacher_form.save(commit=False)
            teacher.is_teacher = True
            teacher.user = user
            teacher.save()
            teacher_form.save_m2m()
            return redirect('teacher_signup')
    else:
        user_form = UserForm
        teacher_form = TeacherForm

    return render(request, 'registration/teacher_signup.html',
                  {'user_form': user_form, 'teacher_form': teacher_form})


@login_required
@user_passes_test(teacher_access)
def StudentView(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        student_form = StudentForm(data=request.POST)

        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            user.save()
            student = student_form.save(commit=False)
            student.is_teacher = False
            student.student = False
            student.user = user
            student.save()
            student_form.save_m2m()
            return redirect('student_signup')
    else:
        user_form = UserForm
        student_form = StudentForm

    return render(request, 'registration/student_signup.html', {'user_form': user_form,
                                                                'student_form': student_form})


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = TeacherForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    # Get the current profile
    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile
