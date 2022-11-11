from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from . import urls


class TestManageBookingView(TestCase):
    
    def test_get_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('index.html')