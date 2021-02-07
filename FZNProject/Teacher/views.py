from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from django.db.models import Count,F
from .models import St,TIntroduce
# from .models import FST
# 引入装饰器函数
from django.contrib.auth.decorators import login_required

# @login_required(login_url='/login/')
def Teacher(request):  #教师页面的展示
    # user = User.objects.get(username=request.user.username)
    # print(user)
    user='1'  #教师的名称
    return render(request,"Teacher_main.html",{"user":user})#返回教师名称

def Teacher_MyStudent(request):#查询选择了教师的学生信息
    # user = User.objects.get(username=request.user.username)
    user='DALI'
    Student_Number=St.objects.filter(tname=user).count() #查询选择了的学生人数
    Students=St.objects.filter(tname=user) #查询选择了的学生的信息 sno和sname
    # print(Student_Number)
    # print(Student.sno)
    return HttpResponse('查询学生人数')

def Teacher_Information(request): #获取教师个人信息
    # Teacher_tno=request.user.username
    Teacher_tno=1
    TeacherInformation=TIntroduce.objects.filter(id=Teacher_tno)
    print(TeacherInformation)
    return HttpResponse('查询教师信息')

def Teacher_InfomationChange(request): #修改教师个人信息
    # Teacher_tno=request.user.username
    Teacher_info_new=request.POST.get('NewInfo') #获取评价
    Teacher_tno=1 #获取教师Tno
    Teacher_info=TIntroduce.objects.get(tno=Teacher_tno) #获取object
    Teacher_info.d_information=Teacher_info_new #修改object
    Teacher_info.save() #确认修改
    return HttpResponse('成功修改信息')

def Teacher_SelectStudent(request): #选择学生
    # SelectSno=request.GET.getlist() #获取选择的学生的sno
    #设置数据表FST存储最终选择
    #Teacher_FS=FST()
    #SlectNum=SelectSno.count
    #for i in range(SlectNum) :
        #Teacher_FS.sno=SelectSno[i].sno
        #Teacher_FS.sname=SelectSno[i].same
        #Teacher_FS.tno=SelectSno[i].tno
        #Teacher_FS.tname=SelectSno[i].tname
        #Teacher_FS.save()
    return HttpResponse('选择成功')
