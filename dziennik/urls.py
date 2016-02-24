from django.conf.urls import patterns, include, url
from django.contrib import admin

import edziennik.views as views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<teacher_id>[0-9]+)/$', views.teacher),
    url(r'^(?P<teacher_id>[0-9]+)/lessons/$', views.lessons),
    url(r'^(?P<teacher_id>[0-9]+)/classes/$', views.classes),
    url(r'^(?P<teacher_id>[0-9]+)/classes/my/$', views.myClasses),
    url(r'^(?P<teacher_id>[0-9]+)/students/$', views.students),
    url(r'^(?P<teacher_id>[0-9]+)/students/my/$', views.myStudents),
    url(r'^(?P<teacher_id>[0-9]+)/classes/(?P<class_id>[0-9]+)/$', views.oneClass),
    url(r'^(?P<teacher_id>[0-9]+)/students/(?P<student_id>[0-9]+)/$', views.oneStudent),
    url(r'^(?P<teacher_id>[0-9]+)/students/create/$', views.createStudent),

    url(r'^admin/', admin.site.urls),
]
