from rest_framework import serializers

from members.serializers import UserSerializer
from .models import Post, Comment

__all__ = (
    'CommentSerializer',
    'PostSerializer',
    'PostCreateSerializer',
    'PostDetailSerializer',
    'PostUpdateSerializer',
)


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = (
            'pk',
            'author',
            'content',
        )


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        fields = (
            'pk',
            'title',
            'author',
            'content',
            'is_published',
        )


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'is_published',

        )

    def to_representation(self, instance):
        return PostSerializer(instance).data


class PostDetailSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'is_published',
            'comment_set',
        )


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'is_published',
        )

    def to_representation(self, instance):
        return PostSerializer(instance).data
