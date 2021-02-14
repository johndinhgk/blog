from django.urls import path
from .import views
from .models import Post
urlpatterns = [
    path('',views.PostListView.as_view(), name = 'blog'),
    path('<int:pk>/',views.post,name = 'post'),
]
