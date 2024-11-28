from django.contrib import admin
from booking.models.address import Address
from booking.models.object import Object
from booking.models.media import ObjectImage, ObjectVideo


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner', 'is_active')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'street', 'house')


@admin.register(ObjectImage)
class ObjectImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'object', 'image')


@admin.register(ObjectVideo)
class ObjectVideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'object', 'video_url')
