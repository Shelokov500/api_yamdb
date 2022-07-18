from django.urls import include, path
<<<<<<< HEAD
from rest_framework.routers import DefaultRouter

from .views import GenreViewSet, CategoryViewSet, TitleViewSet

router_v1 = DefaultRouter()
router_v1.register('title', TitleViewSet, basename='title')
router_v1.register('category', CategoryViewSet, basename='category')
router_v1.register('genre', GenreViewSet, basename='genre')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
=======
from rest_framework import routers

from .views import CommentViewSet, ReviewViewSet

router_v1 = routers.DefaultRouter()
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
>>>>>>> e40479bb661feed86a5080e9b1cb25aee9cc36d3
