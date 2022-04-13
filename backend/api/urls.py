from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('search-thread/<str:query>', views.search_thread, name="search_thread"),
    path('thread-list/<int:category>', views.thread_list, name="thread_list"),
    path('get-categories', views.get_categories, name="get_categories"),
    path('create-categories', views.create_categories, name="create_categories"),
    path('create-thread', views.create_thread, name="create_thread"),
    path('publish-reply', views.publish_reply, name="publish_reply"),
    path('get-comments/<str:uuid>', views.get_comments, name="get_comments"),
    path('get-thread/<str:uuid>', views.get_thread, name="get_thread"),
]
