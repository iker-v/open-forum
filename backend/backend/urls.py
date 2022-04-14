from django.urls import path, include

urlpatterns = [
    path('account/', include('account.urls')),
    path('category/', include('category.urls')),
    path('post/', include('post.urls')),
    path('thread/', include('thread.urls')),
]
