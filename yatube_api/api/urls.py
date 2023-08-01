from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, GroupViewSet, PostViewSet

v1_router = routers.DefaultRouter()
v1_router.register(r'^posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comments')
v1_router.register('groups', GroupViewSet, basename='groups')
v1_router.register('posts', PostViewSet, basename='posts')


urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
