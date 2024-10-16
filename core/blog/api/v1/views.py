from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post

data = {
    "id": 1,
    "title": "hello"
}


@api_view()
def post_list(request):
    return Response("Ok")


@api_view()
def post_detail(request, id):
    post = Post.objects.get(pk=id)
    serializer = PostSerializer(post)
    return Response(serializer.data)
