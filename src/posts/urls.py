from django.urls import path
from .views import PostList, PostDetails, UserDetails, UserList, api_root
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetails.as_view(), name='post-detail'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetails.as_view(), name='user-detail')
])