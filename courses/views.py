from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages
from courses.forms import CourseModelForm, LessonModelForm
from .models import Course


class CourseIndexView(generic.ListView):
    template_name = 'courses/index.html'
    context_object_name = 'courses'

    def get_queryset(self):
        """Return the last five published questions."""
        return Course.objects.all()


class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'courses/detail.html'


def add_course(request):
    form = CourseModelForm
    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            messages.success(request, "Course %s has been successfully added." % (request.POST['name']))
            form.save()
            return redirect('/')

    return render(request, 'courses/add.html', {'form': form})


def edit_course(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)
        if form.is_valid():
            messages.success(request, "The changes have been saved.")
            form.save()
    form = CourseModelForm(instance=course)

    return render(request, 'courses/edit.html', {'form': form})


def remove_course(request, pk):
    course = Course.objects.get(id=pk)
    if request.method == 'POST':
        messages.success(request, "Course %s has been deleted." % course.name)
        course.delete()
        return redirect('courses:index')
    return render(request, 'courses/remove.html', {'course': course.name})


def add_lesson(request, course_id):
    form = LessonModelForm(initial={'course': course_id})
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            messages.success(request, "Lesson %s has been successfully added." % request.POST['name'])
            form.save()
            return redirect('courses:detail', pk=1)

    return render(request, 'courses/add.html', {'form': form})

