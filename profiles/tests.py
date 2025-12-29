from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from profiles.models import Profile

User = get_user_model()


class ProfileAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(id=2, email='user2@example.com', password='1234')
        self.client.force_authenticate(user=self.user)

    def test_create_profile_via_api(self):
        
        self.client.force_authenticate(user=self.user)
        data = {"role": "QA", "contact_number": "1234567890"}
        resp = self.client.post("/api/profiles/", data, format="json")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 1)
