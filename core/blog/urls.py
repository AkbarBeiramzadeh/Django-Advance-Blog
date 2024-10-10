from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic import RedirectView


app_name = 'blog'

urlpatterns = [
    path('fbv-index', views.index_view, name='fbv-index'),
    path('cbv-index', views.IndexView.as_view(), name='cbv-index'),
    path('redirect-to-google',RedirectView.as_view(url='https://google.com'),name='redirect-to-google'),
    path('redirect-to-index',RedirectView.as_view(pattern_name='blog:cbv-index'),name='redirect-to-google'),
]
