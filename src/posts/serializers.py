from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            '_id',
            'title',
            'content',
            'author'
        ]

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    # post = serializers.ReadOnlyField(source='post._id')

    class Meta:
        model = Comment
        fields = [
            '_id',
            'by',
            'published',
            'content',
            'post'
        ]

    # def create(self, validated_data):
    #     print(validated_data)
    #     return Comment.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.save()
    #     return instance
