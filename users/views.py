from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.context_processors import csrf


def index(request):
    return HttpResponse("<p>世界好</p>")


def user_login(request):
    '''
    login
    '''
    if request.POST:
        # TODO 这两个变量必须预先设置为空，不晓得原理
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            print(user)
            return redirect('/users/userInfo')
    ctx = {}
    ctx.update(csrf(request))
    return render(request, 'users/loginForm.html', ctx)


#  实现登出
def user_logout(request):
    """
       logout
       URL: /users/logout
    """
    logout(request)
    return redirect('/users')


def diff_response(request):
    # is_authenticated新版本不需要加（）
    if request.user.is_authenticated:
        content = "<p>my dear "+request.user.get_username()+"</p>"
    else:
        content = "<p>you wired stranger</p>"
    return HttpResponse(content)
