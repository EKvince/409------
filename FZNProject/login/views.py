from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User

# Create your views here.

def login(request):
    if request.method == "POST":
        Accountname = request.POST.get('Account', None)
        password = request.POST.get('Password', None)
        if Accountname and password:  # 确保用户名和密码都不为空
            Accountname = Accountname.strip()
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:
                #user = models.login_user.objects.get(Account=Accountname)
                user = User.objects.get(Account=Accountname)
                print(user)
            except:
                #return render(request, 'login/login.html')
                return HttpResponse('EXCEPT')
            if user.Password == password:
                return redirect('/index/')
               # return HttpResponse('登陆成功')
    #return render(request, 'login/login.html')
    return HttpResponse('你不是POST')