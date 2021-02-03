from rest_framework import serializers
from .models import Post, Comment
from django.http import Http404
from bson.objectid import InvalidId, ObjectId


def get_post(pk):
    try:
        return Post.objects.get(pk=ObjectId(pk))
    except Post.DoesNotExist:
        raise Http404


class ObjectIdField(serializers.Field):
    def to_internal_value(self, data):
        print("SF", data)
        if ObjectId(data):
            return ObjectId(data.strip())
        else:
            raise serializers.ValidationError(InvalidId)

    def to_representation(self, value):
        return str(value)


class PostSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = Post
        fields = [
            # 'url',
            # 'owner',
            'title',
            'content',
            'author'
        ]
    # title = serializers.CharField(max_length=100, allow_blank=False)
    # content = serializers.CharField()
    # author = serializers.CharField(max_length=100, allow_blank=False)

    # def create(self, validated_data):
    #     return Post.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.save()
    #     return instance


class CommentSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    # by = serializers.CharField(max_length=100, allow_blank=False)
    # published = serializers.BooleanField(allow_null=True)
    # content = serializers.CharField()
    post = ObjectIdField(
        required=True
    )

    class Meta:
        model = Comment
        fields = [
            '_id',
            'by',
            'published',
            'content',
            'post'
        ]

    def create(self, validated_data):
        validated_data_with_post = {
            **validated_data,
            'post': get_post(validated_data['post'])
        }
        return Comment.objects.create(**validated_data_with_post)

    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.save()
    #     return instance
