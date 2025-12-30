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
        self.client.force_authenticate(user=self.user)

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
