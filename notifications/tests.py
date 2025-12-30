from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from notifications.models import Notification

User = get_user_model()


class NotificationAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            id=2, email="user16@user15.com", password="1234"
        )
        self.client.force_authenticate(user=self.user)

    def test_get_notifications_and_mark_read(self):
        n = Notification.objects.create(text="You have a message", user=self.user)
        resp = self.client.get("/api/notifications/", format="json")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(resp.data), 1)
        # mark read
        resp2 = self.client.get(f"/api/notifications/{n.id}/mark_read/", format="json")
        self.assertEqual(resp2.status_code, status.HTTP_200_OK)
        n.refresh_from_db()
        self.assertTrue(n.mark_read)
