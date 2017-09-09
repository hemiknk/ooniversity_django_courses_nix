from django.conf.urls import url
from students.views import StudentDetailView, StudentsIndexView, add_student, edit_student, remove_student

app_name = 'students'
urlpatterns = [
    url(r'^$', StudentsIndexView.as_view(), name='list_view'),
    url(r'^add/$', add_student, name='add'),
    url(r'^edit/(?P<pk>[0-9]+)/$', edit_student, name='edit'),
    url(r'^remove/(?P<pk>[0-9]+)/$', remove_student, name='remove'),
    url(r'^(?P<pk>[0-9]+)/$', StudentDetailView.as_view(), name='detail'),
]
