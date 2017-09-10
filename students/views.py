from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from students.forms import StudentModelForm
from .models import Student


class StudentListView(generic.ListView):
    template_name = 'students/list_view.html'
    context_object_name = 'students'
    model = Student

    def get_queryset(self, **kwargs):
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            return Student.objects.filter(courses=course_id)
        return Student.objects.all()


class StudentDetailView(generic.DetailView):
    model = Student
    template_name = 'students/detail.html'


class StudentCreateView(generic.CreateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Student registration'})
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request,
                         "Student %s %s has been successfully added." % (form.instance.name, form.instance.surname))
        return response


class StudentUpdateView(generic.UpdateView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:edit')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Student info update'})
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Info on the student %s %s has been successfully changed." % (
            form.instance.name, form.instance.surname))
        return response


class StudentDeleteView(generic.DeleteView):
    model = Student
    form_class = StudentModelForm
    success_url = reverse_lazy('students:list_view')

    def delete(self,  *args, **kwargs):
        student = Student.objects.get(id=kwargs['pk'])
        messages.success(self.request, "Info on %s  has been successfully deleted." %
                         student.get_name_surname())
        response = super().delete(self, *args, **kwargs)
        return response

    def get_context_data(self, **kwargs):
        student = Student.objects.get(id=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Student info suppression', 'student': student.name})
        return context

