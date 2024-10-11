from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('cbv-index', views.IndexView.as_view(), name='cbv-index'),
    path('go-to-maktab/<int:pk>/', views.RedirectToMaktabView.as_view(), name='redirect-to-maktabkhooneh'),
    path('posts/', views.PostList.as_view(), name='post-list'),
]
