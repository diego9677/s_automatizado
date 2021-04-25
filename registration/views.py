from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegisterForm


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro exitoso')
            return redirect(reverse('index'))
        messages.error(request, 'Error en los datos ingresados')
    context = {
        'form': RegisterForm()
    }
    return render(request, 'registration/register.html', context)
