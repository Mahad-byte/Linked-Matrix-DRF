from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from tasks.models import Task

User = get_user_model()


class TaskAPITest(APITestCase):  # TODO check signal
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

    def test_create_task_via_api(self):
        profile_id = self.user.user_profile.id
        proj_resp = self.client.post(
            "/api/projects/",
            {"title": "Proj Task", "description": "desc"},
            format="json",
        )
        print("create project res: ", proj_resp)
        self.assertEqual(proj_resp.status_code, status.HTTP_201_CREATED)
        project_id = proj_resp.data["id"]
        task_data = {
            "title": "Task A",
            "description": "details",
            "status": "O",
            "project_id": project_id,
            "asignee": profile_id,
        }
        task_resp = self.client.post("/api/tasks/", task_data, format="json")
        print("task creation response: ", task_resp)
        print(task_resp.data)
        self.assertEqual(task_resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertTrue(str(task_resp.data.get("id")))
