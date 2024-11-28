from django.db import models


class Object(models.Model):
    name = models.CharField(
        verbose_name='Название объекта', max_length=64
    )
    number_of_room = models.PositiveSmallIntegerField(
        verbose_name='Количество комнат'
    )
    square = models.PositiveSmallIntegerField(
        verbose_name='Площадь'
    )
    floor = models.PositiveSmallIntegerField(
        verbose_name='Этаж',
    )
    adult = models.PositiveSmallIntegerField(
        verbose_name='Количество взрослых',
    )
    kid = models.PositiveSmallIntegerField(
        verbose_name='Количество детей',
    )
    owner = models.ForeignKey(
        'users.User', verbose_name='Собственник',
        related_name='user_objects', on_delete=models.CASCADE,
    )
    average_rating = models.FloatField(
        verbose_name='Рейтинг объекта', default=0.0
    )
    sea_distance = models.PositiveIntegerField()
    address = models.OneToOneField(
        'address', related_name='object_by_address',
        verbose_name='Адрес', on_delete=models.CASCADE,
    )
    is_active = models.BooleanField(
        default=False, verbose_name='Объявление активно',
    )
    view = models.PositiveIntegerField(
        default=0, verbose_name='Количество просмотров'
    )
    description = models.TextField(
        verbose_name='Описание',
    )
    number_of_floors = models.PositiveIntegerField(
        verbose_name='Количество этажей',
    )

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return f'{self.name}'
