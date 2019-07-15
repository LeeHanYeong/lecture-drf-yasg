from rest_framework import serializers

from .models import Post, Comment

POST_FIELDS = (
    'title',
    'content',
    'is_published',
)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = POST_FIELDS + (
            'pk',
            'author',
            'created',
            'modified',
        )


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = POST_FIELDS


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = POST_FIELDS


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'pk',
            'content',
            'created',
            'modified',
        )
