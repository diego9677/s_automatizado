from django.utils.timezone import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Modem, Action
from .utils import exec_command
from django.contrib import messages


@login_required
def index(request):
    if request.user.is_staff:
        return redirect('/admin')

    now = datetime.now().date()
    action_count = Action.objects.filter(user=request.user, created_at__day=now.day,
                                         created_at__month=now.month).count()

    context = {
        'modem_name': None,
        'status': 'offline',
        'actions': action_count
    }

    try:
        modem = Modem.objects.get(user=request.user)
    except Modem.DoesNotExist as e:
        return render(request, 'core/index.html', context)

    try:
        output = exec_command('admin', 'admin12345', modem.ip, 'system identity print')
        raw_wifi = exec_command('admin', 'admin12345', modem.ip, 'interface wireless print')
        ssid, frequency = raw_wifi.strip().find('ssid'), raw_wifi.strip().find('frequency')
        modem_name = output.strip().replace('name: ', '')
        wifi_name = raw_wifi[ssid: frequency].replace('ssid=', '').replace('"', '').strip()
        context['modem_name'] = modem_name
        context['wifi_name'] = wifi_name
        context['status'] = 'online'

        return render(request, 'core/index.html', context)
    except Exception as e:
        print(e)
        return render(request, 'core/index.html', context)


@login_required
def reboot_system(request, pk):
    if request.method == 'POST':
        now = datetime.now()
        action_count = Action.objects.filter(user=request.user, created_at=now).count()
        if action_count < 3:
            modem = get_object_or_404(Modem, pk=pk)
            output = exec_command('admin', 'admin12345', modem.ip, 'system reboot')
            Action.objects.create(user=request.user)
            print(output)
            messages.success(request, 'Reiniciando')
            return redirect(reverse_lazy('index'))
    messages.error(request, 'Ha ocurrido un error')
    return redirect(reverse_lazy('index'))


@login_required
def change_wifi(request, pk):
    if request.method == 'POST':
        try:
            modem = get_object_or_404(Modem, pk=pk)
            ssid = request.POST.get('ssid', None)
            pwr = request.POST.get('password', None)
            exec_command('admin', 'admin12345', modem.ip,
                         f'interface wireless set numbers=0 ssid="{ssid}";interface wireless security-profiles set numbers=1 wpa-pre-shared-key="{pwr}" wpa2-pre-shared-key="{pwr}"')
            return redirect(reverse_lazy('index'))
        except Exception:
            return redirect(reverse_lazy('index'))
    return redirect(reverse_lazy('index'))
