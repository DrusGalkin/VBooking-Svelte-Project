from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
                                  DestroyModelMixin


class ExtendedView:
    multi_permission_classes = None
    multi_serializer_class = None
    request = None

    def get_serializer_class(self):
        assert self.serializer_class or self.multi_serializer_class, (
                '"%s" should either include `serializer_class`, '
                '`multi_serializer_class`, attribute, or override the '
                '`get_serializer_class()` method.' % self.__class__.__name__
        )
        if not self.multi_serializer_class:
            return self.serializer_class

        # define request action or method
        if hasattr(self, 'action') and self.action:
            action = self.action
        else:
            action = self.request.method

        # Trying to get action serializer or default
        return self.multi_serializer_class.get(action) or self.serializer_class

    def get_permissions(self):
        # define request action or method
        if hasattr(self, 'action'):
            action = self.action
        else:
            action = self.request.method

        if self.multi_permission_classes:
            permissions = self.multi_permission_classes.get(action)
            if permissions:
                return [permission() for permission in permissions]

        return [permission() for permission in self.permission_classes]


class ExtendedGenericViewSet(ExtendedView, GenericViewSet):
    http_method_names = ('get', 'post', 'patch', 'delete')


class CRUDViewSet(ExtendedGenericViewSet, CreateModelMixin,
                  ListModelMixin, RetrieveModelMixin,
                  UpdateModelMixin, DestroyModelMixin):
    pass


class RUDViewSet(ExtendedGenericViewSet,
                 ListModelMixin, RetrieveModelMixin,
                 UpdateModelMixin, DestroyModelMixin):
    pass


class CRDViewSet(ExtendedGenericViewSet, CreateModelMixin,
                 ListModelMixin, RetrieveModelMixin,
                 DestroyModelMixin):
    pass


class UDViewSet(ExtendedGenericViewSet, DestroyModelMixin,
                UpdateModelMixin):
    pass


class CRViewSet(ExtendedGenericViewSet, CreateModelMixin,
                ListModelMixin, RetrieveModelMixin):
    pass


class CRUViewSet(ExtendedGenericViewSet, CreateModelMixin,
                 ListModelMixin, RetrieveModelMixin,
                 UpdateModelMixin):
    pass


class RUViewSet(ExtendedGenericViewSet, RetrieveModelMixin,
                ListModelMixin, UpdateModelMixin):
    pass


class DestroyViewSet(ExtendedGenericViewSet, DestroyModelMixin):
    pass


class ListRetrieveViewSet(ExtendedGenericViewSet, ListModelMixin,
                          RetrieveModelMixin):
    pass


class CreateViewSet(ExtendedGenericViewSet, CreateModelMixin):
    pass
