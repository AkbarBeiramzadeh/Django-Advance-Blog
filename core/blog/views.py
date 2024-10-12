from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from .forms import PostForm
from .models import Post


class IndexView(TemplateView):
    """
    a class  based view to show the index page.
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'ali'
        context['posts'] = Post.objects.all()
        return context


class RedirectToMaktabView(RedirectView):
    url = 'https://maktabkhooneh.org'

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)


class PostList(ListView):
    queryset = Post.objects.all().filter(status=True)
    paginate_by = 7
    # model = Post
    ordering = '-id'
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts

    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/my_post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostCreateView(CreateView):
    model = Post
    # fields = ('author', 'title', 'content', 'status', 'category', 'published_date')
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/blog/post/'
