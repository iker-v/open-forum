from concurrent.futures import thread
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Threads
from django.db.models import Q

@api_view(['GET'])
def search_thread(request, query):
    print(query)
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