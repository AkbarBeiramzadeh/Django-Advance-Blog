from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Post


def index_view(request):
    """
    a function based view to show the index page.
    """
    context = {"name": "ali"}
    return render(request, 'index.html', context=context)


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
