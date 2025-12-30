from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase

from documents.models import Document

User = get_user_model()


class DocumentAPITest(APITestCase):
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

    def test_create_document_via_api(self):
        proj_resp = self.client.post(
            "/api/projects/",
            {
                "title": "Project A",
                "description": "desc",
            },
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
            {
                "title": "Project B",
                "description": "desc",
            },
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

    def test_empty_name_returns_error(self):
        proj_resp = self.client.post(
            "/api/projects/",
            {
                "title": "Project C",
                "description": "desc",
            },
            format="json",
        )
        project_id = proj_resp.data["id"]
        file = SimpleUploadedFile("file.txt", b"file content")
        data = {
            "name": "",
            "description": "desc",
            "file": file,
            "version": 1,
            "project": project_id,
        }
        resp = self.client.post("/api/documents/", data, format="multipart")
        self.assertIn("name", resp.data)
        self.assertTrue(len(resp.data["name"]) > 0)
