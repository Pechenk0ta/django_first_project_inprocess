from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
        else:
            return HttpResponse('Аккаунт не создан')
    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')