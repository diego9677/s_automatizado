from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Modem
from .utils import exec_command
from django.contrib import messages

@login_required
def index(request):
    if request.user.is_staff:
        return redirect('/admin')

    context = {
        'modem_name': None,
        'status': 'offline'
    }

    try:
        modem = Modem.objects.get(user=request.user)
    except Modem.DoesNotExist as e:
        return render(request, 'core/index.html', context)

    try:
        output = exec_command('user1', 'user1', modem.ip, 'system identity print')
        array_command = output.strip().split(':')
        if len(array_command) > 0:
            name = array_command[1].strip()
            context['modem_name'] = name
            context['status'] = 'online'

        return render(request, 'core/index.html', context)
    except Exception as e:
        print(e)
        return render(request, 'core/index.html', context)


def reboot_system(request, pk):
    if request.method == 'POST':
        modem = get_object_or_404(Modem, pk=pk)
        output = exec_command('user1', 'user1', modem.ip, 'system reboot')
        print(output)
        messages.success(request, 'Reiniciando')
        return redirect(reverse_lazy('index'))
    messages.error(request, 'Ha ocurrido un error')
    return redirect(reverse_lazy('index'))
