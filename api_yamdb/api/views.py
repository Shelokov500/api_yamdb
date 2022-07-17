from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter
from reviews.models import Category, Genre, Title

from api.filters import TitleFilter
from api.serializers import (CategorySerializer, GenreSerializer,
                             TitleReadSerializer, TitleSerializer)


class CreateListDeleteViewSet(mixins.CreateModelMixin,
                              mixins.ListModelMixin,
                              mixins.DestroyModelMixin,
                              viewsets.GenericViewSet):
    pass


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    # permission_classes =
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.request.method in ["POST", "PATCH"]:
            return TitleSerializer
        return TitleReadSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    # permission_classes =
    filter_backends = (SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # lookup_field = 'slug'
    # permission_classes =
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
