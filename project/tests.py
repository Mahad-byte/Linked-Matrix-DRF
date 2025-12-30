from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from project.models import Project

User = get_user_model()


class ProjectAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            id=2, email="user16@user15.com", password="1234"
        )
        login_resp = self.client.post(
            "/api/login/",
            {"email": self.user_data["email"], "password": self.user_data["password"]},
            format="json",
        )
        self.assertEqual(login_resp.status_code, status.HTTP_200_OK)
        access = login_resp.data.get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")

        self.user = User.objects.get(email=self.user_data["email"])

    def test_create_project_via_api(self):
        data = {"title": "Proj1", "description": "desc"}
        resp = self.client.post("/api/projects/", data, format="json")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 1)
        self.assertIn("id", resp.data)

    def test_create_project_empty_title(self):
        data = {"title": "   ", "description": "desc"}
        resp = self.client.post("/api/projects/", data, format="json")
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
