from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Categories


@api_view(['GET'])
def get_categories(request):

    categories = Categories.objects.all().values("id", "name", "desc", "image")

    return Response(categories)

@permission_classes(IsAuthenticated)
@api_view(['POST'])
def create_categories(request):

    data = request.data
    category = Categories.objects.create(name=data['name'], desc=data['desc'], image=data['image'])

    return Response()
