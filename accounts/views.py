from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# 그냥 login 이라 하면 중복 
from django.contrib.auth import login as auth_login, logout as auth_logout 


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else: # == 'GET'
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


# session data 를 만드는 것 
def login(request):
    if request.method == 'POST':
        # 얘만 request 가 들어간다 
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')
