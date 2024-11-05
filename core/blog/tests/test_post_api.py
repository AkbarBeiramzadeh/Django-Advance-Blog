from django.urls import reverse
from rest_framework.test import APIClient
import pytest

from accounts.models.users import User


@pytest.mark.django_db
class TestPostApi:

    def test_get_post_response_200_status(self):
        self.user = User(email="foo@bar.com")  # NB: You could also use a factory for this
        password = 'some_password'
        self.user.set_password(password)
        self.user.save()

        # Authenticate client with user
        self.client = APIClient()
        self.client.login(email=self.user.email, password=password)
        url = reverse("blog:api-v1:post-list")
        response = self.client.get(url)

        assert response.status_code == 200
