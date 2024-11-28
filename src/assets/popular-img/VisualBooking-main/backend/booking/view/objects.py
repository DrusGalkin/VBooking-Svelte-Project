from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from common.mixins.view_mixins import CRUDViewSet
from common.pagination import BasePagination
from booking.serializers import objects as object_serializers
from common import permisions as custom_permissions
from booking.models.object import Object
from booking.serializers import media as media_serializers


@extend_schema_view(
    create=extend_schema(
        summary='Создание объекта',
        tags=['Объекты'],
    ),
    list=extend_schema(
        summary='Список объектов',
        tags=['Объекты'],
    ),
    retrieve=extend_schema(
        summary='Детальная информация об объекте.',
        tags=['Объекты'],
    ),
    destroy=extend_schema(
        summary='Удаление объекта',
        tags=['Объекты'],
    ),
    partial_update=extend_schema(
        summary='Обновить объект',
        tags=['Объекты'],
    ),
    add_image=extend_schema(
        summary='Добавить изображения к объекту',
        tags=['Объекты'],

    ),
)
class ObjectView(CRUDViewSet):
    multi_serializer_class = {
        'create': object_serializers.ObjectCreateSerializer,
        'add_images': media_serializers.ObjectImageSerializer,
        'add_videos': media_serializers.ObjectVideoSerializer,
    }
    multi_permission_classes = {
        'create': (custom_permissions.IsOwnerPosition | custom_permissions.IsAdmin,),
    }
    pagination_class = BasePagination
    queryset = Object.objects.all()

    @action(
        detail=True, methods=['post']
    )
    def add_images(self, request, *args, **kwargs):
        instance = self.get_object()
        images_data = []

        for image in request.data.getlist('image'):
            images_data.append({
                'image': image
            })

        serializer = self.get_serializer(data=request.data, context={
            'instance': instance,
            'media': images_data,
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    @action(
        detail=True, methods=['post']
    )
    def add_videos(self, request, *args, **kwargs):
        instance = self.get_object()
        videos_data = []

        for video in request.data.get('video_urls'):
            videos_data.append({
                'video_url': video
            })

        serializer = self.get_serializer(data=request.data, context={
            'instance': instance,
            'media': videos_data,
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
