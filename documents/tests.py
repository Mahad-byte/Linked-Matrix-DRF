from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase

from documents.models import Document

User = get_user_model()


class DocumentAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            id=2, email="user2@example.com", password="1234"
        )
        self.client.force_authenticate(user=self.user)

    def test_create_document_via_api(self):
        proj_resp = self.client.post(
            "/api/projects/",
            {"title": "Project A", "description": "desc"},
            format="json",
        )
        self.assertEqual(proj_resp.status_code, status.HTTP_201_CREATED)
        project_id = proj_resp.data["id"]
        file = SimpleUploadedFile("file.txt", b"file content")
        data = {
            "name": "Doc1",
            "description": "desc",
            "file": file,
            "version": 1,
            "project": project_id,
        }
        resp = self.client.post("/api/documents/", data, format="multipart")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Document.objects.count(), 1)

    def test_missing_file_returns_400(self):
        proj_resp = self.client.post(
            "/api/projects/",
            {"title": "Project B", "description": "desc"},
            format="json",
        )
        project_id = proj_resp.data["id"]
        data = {
            "name": "Doc2",
            "description": "desc",
            "version": 1,
            "project": project_id,
        }
        resp = self.client.post("/api/documents/", data, format="multipart")
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
