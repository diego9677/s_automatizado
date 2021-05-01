from django.db import models


class Modem(models.Model):
    ip = models.CharField(max_length=20, verbose_name='IP', default='0.0.0.0')
    user = models.OneToOneField('registration.User', related_name='modem', on_delete=models.SET_NULL, null=True,
                                blank=True, default=None)
    code = models.CharField(max_length=20, verbose_name='Codigo', unique=True)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = 'modem'
        verbose_name_plural = 'modems'
