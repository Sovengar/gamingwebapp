from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-blog'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog-post_detail'),
    path('post/new/', PostCreateView.as_view(), name='blog-post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='blog-post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='blog-post_delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='blog-user_posts'),
]