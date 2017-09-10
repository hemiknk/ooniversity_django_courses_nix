from django import forms
from courses.models import Course, Lesson


class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = []


class LessonModelForm(forms.ModelForm):
    # def __init__(self, course, *args, **kwargs):
    #     super(LessonModelForm, self).__init__(*args, **kwargs)
    #     self.fields['course'] = course

    class Meta:
        model = Lesson
        exclude = []

