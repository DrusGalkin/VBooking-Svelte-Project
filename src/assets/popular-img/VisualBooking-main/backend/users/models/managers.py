from django.contrib.auth.base_user import BaseUserManager
from rest_framework.exceptions import ParseError


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _check_fields(self):
        res = []
        for field in self.required_fields:
            if not field: res.append(field)
        return res

    def _create_user(
            self, email=None, surname=None, name=None, patronymic=None, password=None, **extra_fields
    ):
        self.required_fields = [surname, name, patronymic, email, password]
        if not self.required_fields:
            raise ParseError(f'Не указаны следующие поля: {self._check_fields()}')

        user = self.model(surname=surname, name=name, patronymic=patronymic, email=email, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
            self, email=None, surname=None, name=None, patronymic=None, password=None, **extra_fields
    ):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        surname = ' ' if surname is None else surname
        name = ' ' if name is None else name
        patronymic = ' ' if patronymic is None else patronymic

        return self._create_user(email, surname, name, patronymic, password, **extra_fields)

    def create_user(
            self, email=None, surname=None, name=None, patronymic=None, password=None, **extra_fields
    ):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)

        return self._create_user(email, surname, name, patronymic, password, **extra_fields)
