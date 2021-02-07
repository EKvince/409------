from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$',views.Student),
    url(r'^MyTeacher$',views.Student_MyTeacher),
    url(r'^Teacher_think$',views.Student_TeacherThink),
    url(r'^Teacher_Exchange$', views.Teacher_Exchange),
]