from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class Title(models.Model):
    name = models.TextField()
    year = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    rating = models.IntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ],
        blank=True,
        null=True,
    )
    description = models.TextField()
    genre = models.ManyToManyField(
        'Genre',
        through='GenreTitle',
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        related_name="title",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['year']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True,
                            max_length=50,)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.genre} {self.title}'
      

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