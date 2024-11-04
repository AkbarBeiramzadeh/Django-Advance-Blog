from django.test import TestCase
from django.urls import reverse, resolve

from blog.views import IndexView


class TestUrl(TestCase):

    def test_blog_index_url_resolve(self):
        url = reverse('blog:cbv-index')
        self.assertEquals(resolve(url).func.view_class, IndexView)
