from rest_framework.permissions import BasePermission
from . import base_position


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.position == base_position.ADMIN_POSITION
        return False


class IsOwnerOfAccount(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return request.user == obj
        return False


class IsOwnerPosition(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.position == base_position.OWNER_POSITION
        return False
