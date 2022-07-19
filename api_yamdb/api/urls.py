from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import GenreViewSet, CategoryViewSet, TitleViewSet, CommentViewSet, ReviewViewSet
from api.views import (UserViewSet, code, signup, token)

router_v1 = DefaultRouter()
router_v1.register('title', TitleViewSet, basename='title')
router_v1.register('category', CategoryViewSet, basename='category')
router_v1.register('genre', GenreViewSet, basename='genre')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)
router_v1.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/signup/', signup, name='signup'),
    path('v1/auth/token/', token, name='login'),
    path('v1/auth/code/', code, name='code'),
]
