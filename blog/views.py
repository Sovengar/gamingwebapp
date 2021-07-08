from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden
from django.db import IntegrityError

from .models import Post, Comment
from .forms import CommentForm

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages

"""
def blog_view(request):

    posts = Post.objects.all()
    if not posts:
        messages.success(self.request, f'There is no posts yet')

    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)
"""

class PostListView(ListView):
    model = Post 
    template_name = 'blog/blog.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5
    ordering = ['-date_posted']

class UserPostListView(ListView):
    model = Post 
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5
    ordering = ['-date_posted']

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class GenrePostListView(ListView):
    model = Post 
    template_name = 'blog/genre_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(genre=self.kwargs.get('genre')).order_by('-date_posted')

class PostDetailView(FormMixin, DetailView):
    model = Post
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm()

        if self.request.user.is_authenticated:
            comment = Comment.objects.filter(author=self.request.user.client).filter(post=self.object)
            if comment.exists():
                context['comment_bool'] = True
            else:
                context['comment_bool'] = False
        else:
            context['comment_bool'] = True
        """
        try:
            Comment.objects.get(author=self.request.user.client)
            context['comment_bool'] = True
        except Comment.DoesNotExist:
            context['comment_bool'] = False
        """
        return context
    
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        form.instance.author = self.request.user.client
        form.instance.post = self.object
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        try:
            form.save()
        except IntegrityError:
            messages.error(self.request, f'Your have already commented on this post')
        except:
            return HttpResponseForbidden()
        return super(PostDetailView, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog-post_detail', kwargs={'pk': self.object.pk})

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'img_prepost', 'genre']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def CommentUpdateView(request, pk):
    comment = Comment.objects.filter(author=request.user.client).filter(post_id=pk).first()
    form = CommentForm(request.POST, initial={'content': Comment.content}, instance=comment)
    form.fields['content'].initial = comment.content
    form['content'].value()
    if form.is_valid():
        form.save()
        return redirect('appsite-index')
    else: 
        print("Invalid form")
        print(form.errors.as_json())
   
    context = {
        'form': form
    }

    return render(request, 'blog/post_detail_update.html', context)

def CommentDeleteView(request, pk):
    Comment.objects.filter(author=request.user.client).filter(post_id=pk).first().delete()
    return redirect('appsite-index')