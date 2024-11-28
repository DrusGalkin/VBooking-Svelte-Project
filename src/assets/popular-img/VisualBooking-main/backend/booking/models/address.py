from django.db import models


class Address(models.Model):
    city = models.CharField(
        verbose_name='Город', max_length=64
    )
    street = models.CharField(
        verbose_name='Улица', max_length=255,
    )
    house = models.PositiveSmallIntegerField(
        verbose_name='Номер дома', null=True, blank=True
    )
    entrance = models.PositiveSmallIntegerField(
        verbose_name='Номер подъезда', null=True, blank=True
    )
    apartment = models.PositiveSmallIntegerField(
        verbose_name='Номер квартиры', null=True, blank=True
    )
    latitude = models.DecimalField(
        verbose_name='Долгота',
        max_digits=9, decimal_places=6
    )
    longitude = models.DecimalField(
        verbose_name='Широта',
        max_digits=9, decimal_places=6,
    )

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return f'{self.city} {self.street} {self.house}'
