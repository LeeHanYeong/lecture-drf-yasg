from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'pk',
            'title',
            'content',
            'is_published',
            'created',
            'modified',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'pk',
            'content',
            'created',
            'modified',
        )
