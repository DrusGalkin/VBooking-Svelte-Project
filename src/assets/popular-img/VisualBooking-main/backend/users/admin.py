from django.contrib import admin
from users.models.position import Position
from users.models.user import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('surname', 'name', 'patronymic', 'email', 'phone', 'position', 'date_joined')
    list_filter = ('position',)
    search_fields = ('email', 'surname', 'name')
    ordering = ('date_joined',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Личные данные', {'fields': ('surname', 'name', 'patronymic', 'phone', 'image', 'position')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'surname', 'name', 'patronymic', 'phone', 'position',
                'image'
            )}
         ),
    )


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)
