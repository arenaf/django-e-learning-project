from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Subject, File
from .forms import SubjectForm, FileForm


# Decorator for teacher links only
def teacher_access(user):
    user_logged = user.profile.is_teacher
    if user_logged:
        return True
    return False


class TeacherRequiredMixin(object):
    @method_decorator(user_passes_test(teacher_access))
    def dispatch(self, request, *args, **kwargs):
        return super(TeacherRequiredMixin, self).dispatch(request, *args, **kwargs)


# SUBJECTS
@method_decorator(login_required, name='dispatch')
class SubjectListView(ListView):
    model = Subject
    template_name = "subject/subject_list.html"


@method_decorator(login_required, name='dispatch')
class SubjectDetailView(DetailView):
    model = Subject
    template_name = "subject/subject_detail.html"


@method_decorator(login_required, name='dispatch')
class SubjectView(TeacherRequiredMixin, CreateView):
    model = Subject
    success_url = reverse_lazy('home')
    form_class = SubjectForm
    template_name = "subject/subject_form.html"


@method_decorator(login_required, name='dispatch')
class SubjectDeleteView(TeacherRequiredMixin, DeleteView):
    model = Subject
    success_url = reverse_lazy('subject')


# FILES
@method_decorator(login_required, name='dispatch')
class FileDetailView(DetailView):
    model = File


@login_required
@user_passes_test(teacher_access)
def FileView(request, id):
    if request.user.is_authenticated:
        file_form = FileForm()
        if request.method == "POST":
            file_form = FileForm(request.POST, request.FILES)
            if file_form.is_valid():
                form = file_form.save(commit=False)
                form.subject_id = id
                form.save()
            return redirect('subject', pk=id)
        return render(request, "subject/file_form.html", {'file_form': file_form})
    else:
        return redirect(reverse_lazy('login'))


@method_decorator(login_required, name='dispatch')
class FileDeleteView(TeacherRequiredMixin, DeleteView):
    model = File
    success_url = reverse_lazy('subject')
