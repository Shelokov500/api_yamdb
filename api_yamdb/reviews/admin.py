from django.contrib import admin
from .models import Title, Category, Genre
from django.contrib.auth.admin import UserAdmin
from reviews.models import User

admin.site.register(Title)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(User, UserAdmin)

# Можно сделать наподобии если останется время
# (смотреть в теории "Регистрация модели Post в админке")
# class PostAdmin(admin.ModelAdmin):
#     # Перечисляем поля, которые должны отображаться в админке
#     list_display = ('text', 'pub_date', 'author') 
#     # Добавляем интерфейс для поиска по тексту постов
#     search_fields = ('text',) 
#     # Добавляем возможность фильтрации по дате
#     list_filter = ('pub_date',)
