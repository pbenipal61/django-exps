from django.urls import path
from .views import PostList, PostDetails, CommentList, CommentDetails
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = format_suffix_patterns([
    path('posts/', PostList.as_view()),
    path('posts/<str:pk>/', PostDetails.as_view()),
    path('comments/', CommentList.as_view()),
    path('comments/<str:pk>/', CommentDetails.as_view()),
])