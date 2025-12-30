from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from comments.models import Comment
from profiles.models import Profile
from project.models import Project
from tasks.models import Task

User = get_user_model()


class CommentAPITest(APITestCase):
    def setUp(self):
        self.user_data = {
            "email": "user16@user15.com",
            "password": "1234",
            "profile": {"role": "Dev", "contact_number": "1234567890"},
        }
        reg_resp = self.client.post("/api/register/", self.user_data, format="json")
        self.assertEqual(reg_resp.status_code, status.HTTP_201_CREATED)

        login_resp = self.client.post(
            "/api/login/",
            {"email": self.user_data["email"], "password": self.user_data["password"]},
            format="json",
        )
        self.assertEqual(login_resp.status_code, status.HTTP_200_OK)
        access = login_resp.data.get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")

        self.user = User.objects.get(email=self.user_data["email"])
        self.profile_id = self.user.user_profile.id

    def test_create_comment_via_api(self):
        proj_resp = self.client.post(
            "/api/projects/",
            {
                "title": "Project B",
                "description": "desc",
            },
            format="json",
        )
        self.assertEqual(proj_resp.status_code, status.HTTP_201_CREATED)
        project_id = proj_resp.data["id"]
        task_data = {
            "title": "Task 1",
            "description": "do something",
            "project_id": project_id,
            "asignee": self.profile_id,
        }
        task_resp = self.client.post("/api/tasks/", task_data, format="json")
        print(task_resp)
        self.assertEqual(task_resp.status_code, status.HTTP_201_CREATED)
        task_id = task_resp.data["id"]
        comment_data = {
            "text": "Nice work",
            "author": self.user.id,
            "task": task_id,
            "project": project_id,
        }
        resp = self.client.post("/api/comments/", comment_data, format="json")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)
