from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializars import SerPosts
from .models import Posts

# Create your views here.
@api_view(['GET'])
def getPosts(request,pk = None):
    if pk:
        obj = Posts.objects.get(id = pk)
        ser = SerPosts(obj,many = False)
        return Response(ser.data)
    objs = Posts.objects.all()
    ser = SerPosts(objs, many = True)
    print(ser.data)
    return Response(ser.data)

@api_view(['POST'])
def postCreate(requset):
    ser = SerPosts(data = requset.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)

@api_view(['POST'])
def postUpdata(request,pk):
    obj = Posts.objects.get(id = pk)
    ser = SerPosts(instance=obj,data = request.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)


@api_view(['DELETE'])
def postDelete(request,pk):
    obj = Posts.objects.get(id=pk)
    obj.delete()
    return Response("item has Deleted")