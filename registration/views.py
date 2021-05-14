from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegisterForm
from core.models import Modem


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            try:
                modem = Modem.objects.get(code=user.ci)
                user.save()
                modem.user = user
                modem.save()
                messages.success(request, 'Usuario creado correctamente.')
                return redirect(reverse_lazy('login'))
            except Modem.DoesNotExist as e:
                messages.error(request, 'La información no es correcta.\nPor favor intenta nuevamente.')
                return redirect(reverse_lazy('signup'))
    context = {
        'form': RegisterForm()
    }
    return render(request, 'registration/register.html', context)
