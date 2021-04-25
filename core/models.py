from django.db import models


class Modem(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    ip = models.CharField(max_length=20, verbose_name='IP')
    mac = models.CharField(max_length=20, verbose_name='Mac')
    user = models.OneToOneField('registration.User', related_name='modem', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'modem'
        verbose_name_plural = 'modems'
