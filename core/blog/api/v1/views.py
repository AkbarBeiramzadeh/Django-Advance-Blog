from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404


@api_view()
def post_list(request):
    posts = Post.objects.filter(status=True)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view()
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, status=True)
    serializer = PostSerializer(post)
    return Response(serializer.data)
