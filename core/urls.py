from django.urls import path
from .views import index, reboot_system

urlpatterns = [
    path('', index, name='index'),
    path('reboot/<int:pk>/', reboot_system, name='reboot')
]
