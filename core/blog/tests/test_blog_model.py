from django.test import TestCase
from blog.models import Post
from datetime import datetime
from accounts.models.users import User
from accounts.models.profiles import Profile


class TestPostModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="test_user@email.com", password="1020")
        self.profile = Profile.objects.create(
            user=self.user,
            first_name="ali",
            last_name="bey",
            description="test descr"
        )

    def test_create_post_with_valid_data(self):
        post = Post.objects.create(
            author=self.profile,
            title="test",
            content="test content",
            status=True,
            category=None,
            published_date=datetime.now()
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertEquals(post.title, "test")
