from rest_framework import generics
from bson.objectid import ObjectId
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


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


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_comment(self, pk):
        try:
            return Comment.objects.get(pk=ObjectId(pk))
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        pk = dict(kwargs)['pk']
        post = self.get_comment(pk)
        serializer = CommentSerializer(post)
        return Response(serializer.data)
