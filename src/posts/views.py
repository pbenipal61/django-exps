from rest_framework import generics
from bson.objectid import ObjectId
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_post(self, pk):
        try:
            return Post.objects.get(pk=ObjectId(pk))
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        pk = dict(kwargs)['pk']
        post = self.get_post(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = dict(kwargs)['pk']
        post = self.get_post(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = dict(kwargs)['pk']
        post = self.get_post(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
