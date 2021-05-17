from django.test import TestCase


class apiTestViews(TestCase):
    def testIndex(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
