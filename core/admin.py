from django.contrib import admin
from .models import Modem, Action


@admin.register(Modem)
class ModemAdmin(admin.ModelAdmin):
    list_display = ('ip', 'user', 'code')
    search_fields = ('ip', 'user__first_name', 'user__last_name', 'code')


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at')
