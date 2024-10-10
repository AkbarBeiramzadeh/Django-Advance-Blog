from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.views.generic import RedirectView


app_name = 'blog'

urlpatterns = [
    path('cbv-index', views.IndexView.as_view(), name='cbv-index'),
    path('go-to-maktab/<int:pk>/',views.RedirectToMaktabView.as_view(), name='redirect-to-maktabkhooneh'),
]
