from django.urls import path
from thread import views

urlpatterns = [
    path('search-thread/<str:query>', views.search_thread, name="search_thread"),
    path('thread-list/<int:category>', views.thread_list, name="thread_list"),
    path('create-thread', views.create_thread, name="create_thread"),
    path('get-thread/<str:uuid>', views.get_thread, name="get_thread"),
    path('up-vote/<str:uuid>', views.up_vote, name="up_vote"),
    path('down-vote/<str:uuid>', views.down_vote, name="down_vote")
]