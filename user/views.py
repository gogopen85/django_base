from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password, make_password

# Create your views here.
def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        passwordConfirm = request.POST.get('passwordConfirm', None)

        res_data = {}

        if not (username and password and passwordConfirm):
            res_data['error'] = ('모든 값을 입력해야합니다.')
            return render(request, 'register.html', res_data)
        elif password != passwordConfirm:
            res_data['error'] = ('비밀번호를 다시한번 확인해주세요.')
            return render(request, 'register.html', res_data)
        else:
            user = User(
                username=username,
                password=make_password(password)
            )
            user.save()

        return render(request, 'register.html', res_data)