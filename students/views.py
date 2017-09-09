from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages

from students.forms import StudentModelForm
from .models import Student


class StudentsIndexView(generic.ListView):
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


def add_student(request):
    form = StudentModelForm
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            messages.success(request, "Student %s %s has been successfully added." % (
                request.POST['name'], request.POST['surname']))
            form.save()
            return redirect('students:list_view')

    return render(request, 'students/add.html', {'form': form})


def edit_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=student)
        if form.is_valid():
            messages.success(request, "Info on the student has been successfully changed.")
            form.save()
    form = StudentModelForm(instance=student)

    return render(request, 'students/edit.html', {'form': form})


def remove_student(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, "Info on %s  has been successfully deleted." %
                         student.get_name_surname())
        return redirect('students:list_view')

    student = student.get_name_surname()

    return render(request, 'students/remove.html', {'student': student})
