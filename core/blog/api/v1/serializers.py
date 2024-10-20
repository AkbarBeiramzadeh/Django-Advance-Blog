from rest_framework import serializers
from ...models import Post, Category


# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)


class PostSerializer(serializers.ModelSerializer):
    # content = serializers.ReadOnlyField()
    # or
    # content = serializers.CharField(read_only=True)
    # or
    # appending to read_only_fields list in Meta class

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'content', 'status', 'created_date', 'published_date')
        read_only_fields = ['content']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)
