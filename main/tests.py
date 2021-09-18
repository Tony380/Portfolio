from django.test import TestCase
from django.urls import reverse


class TestPortfolio(TestCase):
    """Test all views"""

    def test_index_view(self):
        response = self.client.get(reverse('main:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_404_view(self):
        response = self.client.get('/test404')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')
