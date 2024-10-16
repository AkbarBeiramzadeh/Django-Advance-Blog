from rest_framework.decorators import api_view
from rest_framework.response import Response

data = {
    "id": 1,
    "title":"hello"
}


@api_view()
def post_list(request):
    return Response("Ok")


@api_view()
def post_detail(request, id):
    return Response(data)
