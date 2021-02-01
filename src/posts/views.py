from rest_framework import generics
from bson.objectid import ObjectId
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        pk = dict(kwargs)['pk']
        post = Post.objects.get(pk=ObjectId(pk))
        serializer = PostSerializer(post)
        return Response(serializer.data)





