from django.contrib.auth.models import User
from django.test import Client, RequestFactory, TestCase

from .constants import TEST_PASSWORD, TEST_USER, TEST_VIEWS_LIST


class ViewsTest(TestCase):
    def setUp(self):
        self.test_url_names = TEST_VIEWS_LIST
        self.client = Client()
        self.user = self.client.login(username=TEST_USER, password=TEST_PASSWORD)

    def test_urls(self):
        for test_url in self.test_url_names:
            with self.subTest(test_url=test_url["url"]):
                url = test_url["url"]
                self.assertEqual(url, test_url["expected"])

    def test_urls_after_login_returns_200(self):
        for test_url in self.test_url_names:
            with self.subTest(test_url=test_url["url"]):
                response = self.client.get(test_url["url"], follow=True)
                self.assertEquals(response.status_code, 200)
