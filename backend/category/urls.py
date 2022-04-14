from django.urls import path
from category import views

urlpatterns = [
    path('get-categories', views.get_categories, name="get_categories"),
    path('create-categories', views.create_categories, name="create_categories"),
]
