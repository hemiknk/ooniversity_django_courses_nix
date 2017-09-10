from django.shortcuts import render, redirect
from django.urls import reverse_lazy
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


class CourseCreateView(generic.CreateView):
    model = Course
    template_name = 'courses/add.html'
    form_class = CourseModelForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Course creation'})
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request,
                         "Course %s has been successfully added." % form.instance.name)
        return response


class CourseUpdateView(generic.UpdateView):
    model = Course
    form_class = CourseModelForm
    template_name = 'courses/edit.html'

    def get_success_url(self):
        return reverse_lazy('courses:edit', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Course update'})
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "The changes have been saved.")
        return response


class CourseDeleteView(generic.DeleteView):
    model = Course
    form_class = CourseModelForm
    success_url = reverse_lazy('index')

    def delete(self, *args, **kwargs):
        course = Course.objects.get(id=kwargs['pk'])
        messages.success(self.request, "Course %s has been deleted." % course.name)
        response = super().delete(self, *args, **kwargs)
        return response

    def get_context_data(self, **kwargs):
        course = Course.objects.get(id=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Course deletion', 'course': course.name})
        return context


def add_lesson(request, course_id):
    form = LessonModelForm(initial={'course': course_id})
    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            messages.success(request, "Lesson %s has been successfully added." % request.POST['name'])
            form.save()
            return redirect('courses:detail', pk=1)

    return render(request, 'courses/add.html', {'form': form})
