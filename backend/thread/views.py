from concurrent.futures import thread
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Threads, Upvotes, Downvotes
from post.models import Posts
from django.db.models import Q, Count, Exists, OuterRef

@api_view(['GET'])
def search_thread(request, query):
    print(query)
    threads = Threads.objects.filter(
        Q(title__contains=query) &
        Q(show=True)
    ).values("uuid", "title", "created_at")

    return Response(threads)

@api_view(['GET'])
def thread_list(request, category, numThreads):

    threads = Threads.objects.filter(
        Q(category_id=category),
        Q(show=True)
    ).values(
        "uuid",
        "title",
        "desc",
        "created_at",
        "user__username"
    ).annotate(
        upvote=Count('upvotes'),
        downvote=Count('downvotes'),
        post=Count('posts'),
		checkup=Exists(Upvotes.objects.filter(
            Q(user_id=request.user.id) & Q(thread_id=OuterRef('uuid')
        ))),
		checkdown=Exists(Downvotes.objects.filter(
            Q(user_id=request.user.id) & Q(thread_id=OuterRef('uuid')
        )))
    )[numThreads: numThreads+5]

    return Response(threads)

@permission_classes(IsAuthenticated)
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
    ).values(
        "uuid",
        "title",
        "desc",
        "user__username", 
        "user__date_joined",
    ).annotate(
        upvote=Count('upvotes'),
        downvote=Count('downvotes'),
		checkup=Exists(Upvotes.objects.filter(
            Q(user_id=request.user.id) & Q(thread_id=OuterRef('uuid')
        ))),
		checkdown=Exists(Downvotes.objects.filter(
             Q(user_id=request.user.id) & Q(thread_id=OuterRef('uuid')
        )))
    )
    
    post = Posts.objects.filter(thread_id=uuid).values("user__username", "comment", "date")


    return Response({'thread': thread, 'post' : post})

@permission_classes(IsAuthenticated)
@api_view(['POST'])
def up_vote(request, uuid):

    up_filter = Upvotes.objects.filter(
        Q(thread_id=uuid) & Q(user_id=request.user.id)
    )

    if(up_filter.exists()):
        up_filter.delete()
    else:
        Downvotes.objects.filter(
            Q(thread_id=uuid) & Q(user_id=request.user.id)
        ).delete()
        Upvotes.objects.create(thread_id=uuid, user_id=request.user.id)

    up_votes = Upvotes.objects.filter(thread_id=uuid).count()
    down_votes = Downvotes.objects.filter(thread_id=uuid).count()

    return Response({ 'up_votes' : up_votes, 'down_votes' : down_votes})

@permission_classes(IsAuthenticated)
@api_view(['POST'])
def down_vote(request, uuid):

    down_filter = Downvotes.objects.filter(
        Q(thread_id=uuid) & Q(user_id=request.user.id)
    )
    
    if(down_filter.exists()):
        down_filter.delete()
    else:
        Upvotes.objects.filter(
            Q(thread_id=uuid) & Q(user_id=request.user.id)
        ).delete()
        Downvotes.objects.create(thread_id=uuid, user_id=request.user.id)
        

    down_votes = Downvotes.objects.filter(thread_id=uuid).count()
    up_votes = Upvotes.objects.filter(thread_id=uuid).count()

    return Response({ 'up_votes' : up_votes, 'down_votes' : down_votes})