from concurrent.futures import thread
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Posts
from django.db.models import Q
import json



@api_view(['POST'])
def publish_reply(request):

    post = Posts.objects.create(
        user_id=request.user.id,
        thread_id=request.data['thread_uuid'],
        comment=request.data['comment']
    )

    post = Posts.objects.filter(thread_id=post.thread_id).values("user__username", "comment", "date")

    return Response(post)

@api_view(['GET'])
def get_comments(request, uuid):

    post = Posts.objects.filter(thread_id=uuid).values("user__username", "comment", "date")

    return Response(post)