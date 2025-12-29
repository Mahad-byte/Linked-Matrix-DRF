import uuid

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.serializers import RegisterSerializer

# Create your tests here.
User = get_user_model()


class UserAPITest(APITestCase):  # TODO
    def test_user_create(self):
        url = reverse("register")
        data = {
            "email": "user16@user15.com",
            "password": "1234",
            "profile": {"role": "QA", "contact_number": "1234567890"},
        }
        response = self.client.post(url, data, format="json")
        print("Data: ", response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_invalid_email(self):
        url = reverse("register")
        data = {"email": "not-an-email", "password": "1234"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)

    def test_duplicate_email(self):
        url = reverse("register")
        data = {"email": "user16@user15.com", "password": "1234"}
        response1 = self.client.post(url, data, format="json")
        print("duplicate: ", response1.data)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        # Attempt to register same email again
        response2 = self.client.post(url, data, format="json")
        print("duplicate2: ", response2.data)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.filter(email="user16@user15.com").count(), 1)
