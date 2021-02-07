from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models import Count,F
from .models import St,TIntroduce
#from .models import Teacher,Comment
# from .models import Teacher
# 引入装饰器函数
from django.contrib.auth.decorators import login_required


def Student(request):
    pass
    return HttpResponse('学生页面')

def Student_MyTeacher(request): #查看导师信息
    Tno=request.GET.get('Tno')
    TeacherInfo1=TIntroduce.objects.get(tno=Tno)
    # TeacherInfo2=Teacher.objects.get(tno=Tno)
    return HttpResponse('获取信息成功')

def Student_TeacherThink(request): #导师评论
    Sno = User.objects.get(username=request.user.username)
    Tno=St.objects.get(id=Sno)
    #Think=Comment()
    #Think.Tno=Tno
    #Think.Message=request.POST.get('Message')
    #Think.save()
    return HttpResponse('评论成功')

def Teacher_Exchange(request): #退选导师
    Sno = User.objects.get(username=request.user.username)
    Tno=St.objects.get(id=Sno)
    st=St.objects.get(sno=Sno)
    st.delete()
    return HttpResponse('退选成功')