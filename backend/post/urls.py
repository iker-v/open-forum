from django.urls import path
from post import views

urlpatterns = [
    path('publish-reply', views.publish_reply, name="publish_reply"),
    path('get-comments/<str:uuid>', views.get_comments, name="get_comments"),
]