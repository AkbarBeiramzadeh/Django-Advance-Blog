from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404
from rest_framework import status

from rest_framework.views import APIView


class PostList(APIView):
    """
    getting a list of posts and creating new posts
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request):
        """retrieving a list of posts"""
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, status=True)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail": "item removed successfully"}, status=status.HTTP_200_OK)


class PostDetail(APIView):
    """
    getting detail of the post and edit plus removing it.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request, pk):
        """retrieving the post data"""
        post = get_object_or_404(Post, pk=pk, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def put(self, request, pk):
        """editing the post data"""
        post = get_object_or_404(Post, pk=pk, status=True)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        """ deleting the post object """
        post = get_object_or_404(Post, pk=pk, status=True)
        post.delete()
        return Response({"detail": "item removed successfully"}, status=status.HTTP_200_OK)
