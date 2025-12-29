from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from tasks.models import Task

User = get_user_model()


class TaskAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(id=2, email='user2@example.com', password='1234')
        self.client.force_authenticate(user=self.user)

    def test_create_task_via_api(self): # TODO
        prof_resp = self.client.post("/api/profiles/", {"role": "Dev", "contact_number": "1234567890"}, format="json")
        self.assertEqual(prof_resp.status_code, status.HTTP_201_CREATED)
        profile_id = prof_resp.data["id"]
        proj_resp = self.client.post("/api/projects/", {"title": "Proj Task", "description": "desc"}, format="json")
        self.assertEqual(proj_resp.status_code, status.HTTP_201_CREATED)
        project_id = proj_resp.data["id"]
        task_data = {"title": "Task A", "description": "details", "status": "O", "project": project_id, "asignee": profile_id}
        task_resp = self.client.post("/api/tasks/", task_data, format="json")
        self.assertEqual(task_resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertTrue(str(task_resp.data.get("id")))
