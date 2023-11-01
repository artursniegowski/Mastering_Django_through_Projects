"""
Tests for the health check of the web app
"""
from django.test import TestCase
from django.urls import reverse


class HealthCheckTests(TestCase):
    """Test the health check of the web app"""
    def test_health_check_view(self):
        """Test health check view"""
        url_health_check = reverse('app_core:health-check')
        response = self.client.get(url_health_check)
        # check if the data actually is ok
        self.assertEqual(response.status_code, 200) 
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'healthy'}
        )
