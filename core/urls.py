from django.urls import path
from .views import index, reboot_system, change_wifi

urlpatterns = [
    path('', index, name='index'),
    path('reboot/<int:pk>/', reboot_system, name='reboot'),
    path('change/wifi/<int:pk>/', change_wifi, name='change-wifi')
]
