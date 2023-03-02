from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .serializars import SerPosts
from .models import Posts

# Class based viwe
class retrievePosts(generics.RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = SerPosts 

class listCreatePost(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = SerPosts

    def perform_create(self, serializer):
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = serializer.validated_data.get("title")
        serializer.save(content = content)
        
class updatePost(generics.UpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = SerPosts
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

class deletePost(generics.DestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = SerPosts
    lookup_field = 'pk'


