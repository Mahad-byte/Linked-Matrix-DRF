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
