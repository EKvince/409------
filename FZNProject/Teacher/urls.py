from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$',views.Teacher),
    url(r'^MyStudents$',views.Teacher_MyStudent),
    url(r'^MyInfo$',views.Teacher_Information),
]