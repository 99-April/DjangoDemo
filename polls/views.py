import random

from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def toLogin_view(request):
    return render(request, 'login.html')

def Login_view(request):
    u = request.POST.get("user", '')
    p = request.POST.get("pwd", '')

    if u and p:
        c = PollsStudentinfo.objects.filter(stu_name=u, stu_psw=p).count()
        if c >= 1:
            return HttpResponse("登录成功")
        else:
            return HttpResponse("账号密码错误")
    else:
        return HttpResponse("请输入正确的账号和密码")

def toregister_view(request):
    return render(request,'register.html')

def register_view(request):
    u = request.POST.get("user", '')
    p = request.POST.get("pwd", '')
    if u and p:
        stu = PollsStudentinfo(stu_id=random.choice('012456789'),stu_name=u,stu_psw=p)
        stu.save()
        return HttpResponse("注册成功")
    else:
        return HttpResponse("请输入完整的账号和密码")
