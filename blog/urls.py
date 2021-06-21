from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, GenrePostListView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-blog'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='blog-post_detail'),
    path('post/new/', PostCreateView.as_view(), name='blog-post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='blog-post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='blog-post_delete'),
    path('post/user/<str:username>/', UserPostListView.as_view(), name='blog-user_posts'),
    path('post/genre/<str:genre>/', GenrePostListView.as_view(), name='blog-genre_posts'),
    path('post/<int:pk>/comment/update/', CommentUpdateView, name='blog-post_comment_update'),
    path('post/<int:pk>/comment/delete/', CommentDeleteView, name='blog-post_comment_delete')
]