from rest_framework import serializers
from django.db.models import Avg

from reviews.models import Category, Genre, Title


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('__all__')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
    )
    genre = GenreSerializer(
        many=True,
        required=False,
    )

    class Meta:
        model = Title
        fields = ('__all__')


class TitleReadSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True, many=True)
    category = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
    )
    rating = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = Title

    def get_rating(self, obj):
        rating = obj.reviews.aggregate(Avg('score'))['score__avg']
        if isinstance(rating, int):
            return round(rating)
        return rating


class CategorySerializer(serializers.ModelSerializer):
    titles = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
    )

    class Meta:
        model = Category
        fields = ('__all__')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
