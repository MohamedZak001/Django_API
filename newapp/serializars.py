from .models import Posts
from rest_framework import serializers

class SerPosts(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = [
            'author',
            'title',
            'content',
        ]