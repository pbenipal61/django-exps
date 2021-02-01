from django.urls import path
from .views import PostList, PostDetails, UserDetails, UserList
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetails.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetails.as_view())
])