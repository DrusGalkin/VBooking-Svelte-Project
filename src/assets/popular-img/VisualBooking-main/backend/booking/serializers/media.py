import pdb

from django.db.models import Max
from rest_framework import serializers
from booking.models.media import ObjectImage, ObjectVideo


class BaseMediaMixin:
    def create(self, validated_data):
        instance = self.context.get('instance')
        media_data = self.context.get('media')
        media_instances = []

        for data in media_data:
            data['order'] = getattr(
                instance, 'images' if self.Meta.model == ObjectImage else 'videos'
            ).all().aggregate(Max('order'))['order__max'] or 0
            data['order'] += 1

            image_instance = self.Meta.model.objects.create(object=instance, **data)
            media_instances.append(image_instance)

        return media_instances


class ObjectImageSerializer(BaseMediaMixin, serializers.ModelSerializer):

    class Meta:
        fields = (
            'image',
            'order',
        )
        model = ObjectImage
        read_only_fields = ('order',)


class ObjectVideoSerializer(BaseMediaMixin, serializers.ModelSerializer):
    video_urls = serializers.ListSerializer(child=serializers.URLField())

    class Meta:
        fields = (
            'video_urls',
            'order',
        )
        model = ObjectVideo
        read_only_fields = ('order',)
