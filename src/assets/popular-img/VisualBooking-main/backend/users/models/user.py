from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from users.models.managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name='Почта', unique=True, blank=True, null=True,
    )
    phone = models.CharField(
        verbose_name='Номер телефона', unique=True, blank=True, null=True,
    )
    position = models.ForeignKey(
        'Position', verbose_name='Должность',
        related_name='users', on_delete=models.RESTRICT,
        null=True,
    )
    surname = models.CharField(
        verbose_name='Фамилия', max_length=25,
    )
    name = models.CharField(
        verbose_name='Имя', max_length=25,
    )
    patronymic = models.CharField(
        verbose_name='Отчество', max_length=25,
    )
    image = models.ImageField(
        upload_to='users/%Y/%m/%d/', null=True, blank=True,
    )
    date_joined = models.DateField(
        auto_now=True, editable=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['surname', 'name', 'patronymic']

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    groups = models.ManyToManyField(
        Group,
        verbose_name='Группы',
        related_name='custom_user_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='Разрешения',
        related_name='custom_user_set',
        blank=True
    )

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'
