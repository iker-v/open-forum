from concurrent.futures import thread
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CustomUser, Threads, Categories, Posts
from django.db.models import Q
import json


@api_view(['GET'])
def get_categories(request):

    categories = Categories.objects.all().values("id", "name", "desc", "image")

    return Response(categories)

@api_view(['POST'])
def create_categories(request):

    data = request.data
    category = Categories.objects.create(name=data['name'], desc=data['desc'], image=data['image'])

    return Response()
    


# Create your views here.
