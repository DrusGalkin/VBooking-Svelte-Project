from django.db import models


class Position(models.Model):
    code = models.CharField(
        verbose_name='Код роли', max_length=25,
        primary_key=True
    )
    name = models.CharField(
        verbose_name='Роль', max_length=25,
    )

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return f'{self.name}'
