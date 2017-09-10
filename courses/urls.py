from django.conf.urls import url
from courses.views import *

app_name = 'courses'
urlpatterns = [
    url(r'^add/$', add_course, name='add'),
    url(r'^add_lesson/(?P<course_id>[0-9]+)/$', add_lesson, name='add_lesson'),
    url(r'^edit/(?P<pk>[0-9]+)/$', edit_course, name='edit'),
    url(r'^remove/(?P<pk>[0-9]+)/$', remove_course, name='remove'),
    url(r'^(?P<pk>[0-9]+)/$', CourseDetailView.as_view(), name='detail'),
]
