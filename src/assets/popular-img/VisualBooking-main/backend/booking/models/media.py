from os import path
from uuid import uuid4
from django.db import models


def object_directory_path(instance, filename):
    _, ext = path.splitext(filename)
    return f'object_{instance.object.id}/{uuid4().hex + ext}'


class ObjectImage(models.Model):
    image = models.ImageField(
        verbose_name='Изображение', upload_to=object_directory_path,
    )
    object = models.ForeignKey(
        'Object', verbose_name='Объект', on_delete=models.CASCADE,
        related_name='images',
    )
    order = models.PositiveSmallIntegerField(
        verbose_name='Порядок картинки',
    )

    class Meta:
        verbose_name = 'Изображение объекта'
        verbose_name_plural = 'Изображения объектов'


class ObjectVideo(models.Model):
    video_url = models.URLField(
        verbose_name='Ссылка на видео',
    )
    object = models.ForeignKey(
        'Object', verbose_name='Объект', on_delete=models.CASCADE,
        related_name='videos',
    )
    order = models.PositiveSmallIntegerField(
        verbose_name='Порядок видео',
    )

    class Meta:
        verbose_name = 'Видео объекта'
        verbose_name_plural = 'Видео объектов'
