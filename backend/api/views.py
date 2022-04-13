from concurrent.futures import thread
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser, Threads, Categories, Posts
from django.db.models import Q
import json

@api_view(['GET'])
def search_thread(query):

    threads = Threads.objects.filter(
        Q(title__contains=query) &
        Q(show=True)
    ).values("uuid", "title", "created_at")

    return Response(threads)

@api_view(['GET'])
def thread_list(request, category):

    threads = Threads.objects.filter(
        Q(category_id=category),
        Q(show=True)
    ).values("uuid", "title", "desc", "created_at", "user__username")

    return Response(threads)

@api_view(['POST'])
def publish_reply(request):

    post = Posts.objects.create(
        user_id=request.user.id,
        thread_id=request.data['thread_uuid'],
        comment=request.data['comment']
    )

    post = Posts.objects.filter(id=post.id).values("user__username", "comment", "date")

    return Response({'post': post})

@api_view(['GET'])
def get_comments(request, uuid):

    post = Posts.objects.filter(thread_id=uuid).values("user__username", "comment", "date")

    return Response(post)

@api_view(['GET'])
def get_categories(request):

    categories = Categories.objects.all().values("id", "name", "desc", "image")

    return Response(categories)

@api_view(['POST'])
def create_categories(request):

    data = request.data
    category = Categories.objects.create(name=data['name'], desc=data['desc'], image=data['image'])

    return Response()
    
@api_view(['POST'])
def create_thread(request):
    data = request.data

    thread = Threads.objects.create(
        title=data['title'],
        desc=data['content'],
        user_id=request.user.id,
        category_id=data['category'], 
        show=True
    )

    return Response({'thread_id': thread.uuid})

@api_view(['GET'])
def get_thread(request, uuid):

    thread = Threads.objects.filter(
        Q(uuid=uuid) & Q(show=True)
    ).values("title", "desc", "user__username", "user__date_joined")
    
    post = Posts.objects.filter(thread_id=uuid).values("user__username", "comment", "date")


    return Response({'thread': thread, 'post' : post})

# Create your views here.
