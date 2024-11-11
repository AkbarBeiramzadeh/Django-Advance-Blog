from locust import HttpUser, task, between


class QuickstartUser(HttpUser):

    def on_start(self) -> None:
        response = self.client.post('/accounts/api/v2/jwt/create/', data={
            "email": "admin@admin.com",
            "password": "AsAs1020"
        }).json()
        self.client.headers = {"Authorization": f"Bearer {response.get('access', None)}"}

    @task
    def post_list(self):
        self.client.get("/api/v1/post/")

    @task
    def post_category(self):
        self.client.get("/api/v1/category/")
