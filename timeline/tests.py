from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from project.models import Project
from timeline.models import Timeline

User = get_user_model()


class TimelineAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            id=2, email="user16@user15.com", password="1234"
        )
        self.client.force_authenticate(user=self.user)

    def test_timeline_list_includes_created(self):

        proj_resp = self.client.post(
            "/api/projects/",
            {"title": "ProjTime", "description": "desc"},
            format="json",
        )
        self.assertEqual(proj_resp.status_code, status.HTTP_201_CREATED)
        project_id = proj_resp.data["id"]
        project = Project.objects.get(id=project_id)
        Timeline.objects.create(event_type="C", project=project)
        resp = self.client.get("/api/timeline/", format="json")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(resp.data), 1)
