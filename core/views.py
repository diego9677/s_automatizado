from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Modem
from .utils import exec_command


@login_required
def index(request):
    ip = request.user.modem.ip
    output = exec_command('user1', '12345678', ip, 'system identity print')
    array_command = output.strip().split(':')
    context = {
        'modem_name': None
    }
    if len(array_command) > 0:
        name = array_command[1].strip()
        context['modem_name'] = name
    return render(request, 'core/index.html', context)


def reboot_system(request, pk):
    if request.method == 'POST':
        modem = get_object_or_404(Modem, pk=pk)
        output = exec_command('user1', '12345678', modem.ip, 'system reboot')
        print(output)
        return redirect(reverse_lazy('index') + '?msg=ok')
    return redirect(reverse_lazy('index') + '?msg=error')
