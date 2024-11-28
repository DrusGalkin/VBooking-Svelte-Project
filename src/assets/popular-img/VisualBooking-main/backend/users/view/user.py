from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema_view, extend_schema
from common.mixins.view_mixins import CRUDViewSet
from users.serializers import user as user_serializers
from rest_framework import permissions
from common import permisions as custom_permissions
from common.pagination import BasePagination

User = get_user_model()


@extend_schema_view(
    create=extend_schema(
        summary='Регистрация',
        tags=['Пользователи'],
        description='Регистрация только для не авторизированных пользователей. '
                    '(то-есть без заголовка authentication в запросе'
    ),
    list=extend_schema(
        summary='Список пользователей',
        tags=['Пользователи'],
        description='Список пользователей, информация о пользователях короткая,'
                    'для полной информации есть другая точка. Доступна только админу.'
    ),
    retrieve=extend_schema(
        summary='Детальная информация о пользователе.',
        tags=['Пользователи'],
        description='Детальная информация о пользователе по id. Доступна только админу.'
    ),
    destroy=extend_schema(
        summary='Удаление пользователя',
        tags=['Пользователи'],
        description='Доступна только админу.'
    ),
    partial_update=extend_schema(
        summary='Обновить пользователя',
        tags=['Пользователи'],
        description='Обновлять можно почту, телефон, ФИО. Доступно владельцу аккаунта или админу'
    )
)
class UserView(CRUDViewSet):
    queryset = User.objects.all()
    multi_serializer_class = {
        'create': user_serializers.UserRegistrationSerializer,
        'list': user_serializers.UserListSerializer,
        'retrieve': user_serializers.UserDetailSerializer,
        'partial_update': user_serializers.UserUpdateSerializer,
    }
    multi_permission_classes = {
        'create': (~permissions.IsAuthenticated,),
        'list': (custom_permissions.IsAdmin,),
        'retrieve': (custom_permissions.IsAdmin,),
        'partial_update': (custom_permissions.IsOwnerOfAccount | custom_permissions.IsAdmin,),
        'destroy': (custom_permissions.IsAdmin,)
    }

    pagination_class = BasePagination
