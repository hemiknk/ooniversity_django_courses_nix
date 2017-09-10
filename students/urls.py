from django.conf.urls import url
from students.views import *

app_name = 'students'
urlpatterns = [
    url(r'^$', StudentListView.as_view(), name='list_view'),
    url(r'^add/$', StudentCreateView.as_view(), name='add'),
    url(r'^edit/(?P<pk>[0-9]+)/$', StudentUpdateView.as_view(), name='edit'),
    url(r'^remove/(?P<pk>[0-9]+)/$', StudentDeleteView.as_view(), name='remove'),
    url(r'^(?P<pk>[0-9]+)/$', StudentDetailView.as_view(), name='detail'),
]
