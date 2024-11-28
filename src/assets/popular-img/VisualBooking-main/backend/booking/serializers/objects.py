from rest_framework import serializers
from booking.models.object import Object
from common.mixins.serializer_mixins import CommonMixin
from booking.models.address import Address


class AddressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'city',
            'street',
            'house',
            'entrance',
            'apartment',
            'longitude',
            'latitude',
        )


class ObjectValidate(CommonMixin):
    def validate(self, attrs):
        attrs = self.to_capitalize(attrs, ['name', 'description'])
        return attrs


class ObjectCreateSerializer(ObjectValidate, serializers.ModelSerializer):
    address = AddressCreateSerializer()

    class Meta:
        model = Object
        fields = (
            'name',
            'description',
            'adult',
            'kid',
            'sea_distance',
            'number_of_room',
            'number_of_floors',
            'square',
            'floor',
            'address',
        )

    def create(self, validated_data):
        address_data = validated_data.pop('address')

        address_serializer = AddressCreateSerializer(data=address_data)
        address_serializer.is_valid(raise_exception=True)
        address_instance = address_serializer.save()

        object_instance = self.Meta.model.objects.create(
            address=address_instance,
            owner=self.context.get('request').user,
            **validated_data
        )
        return object_instance
