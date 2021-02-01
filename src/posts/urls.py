from django.urls import path
from .views import PostList, PostDetails
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    path('posts/', PostList.as_view()),
    path('posts/<str:pk>/', PostDetails.as_view())
])