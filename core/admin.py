from django.contrib import admin
from .models import Modem


@admin.register(Modem)
class ModemAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip', 'mac')
