from django.db import models
from django.contrib.auth.models import AbstractUser


ROLE_CHOICES = (
    ('user', 'Пользователь'),
    ('admin', 'Администратор'),
    ('moderator', 'Модератор')
)


class User(AbstractUser):
    bio = models.TextField('Биография', blank=True)
    email = models.EmailField('Адрес электронной почты', unique=True)
    role = models.CharField('Роль', max_length=255, choices=ROLE_CHOICES,
                            default='user')

    def __str__(self) -> str:
        return self.username

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    @property
    def is_user(self):
        return self.role == 'user'
