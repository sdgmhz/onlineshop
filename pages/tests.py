from django.test import TestCase
from django.urls import reverse


class TestPagesApp(TestCase):
    def test_home_page_url(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_url_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_page_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Home Page")

    def test_home_page_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, 'pages/home.html')

    def test_about_us_page_url(self):
        response = self.client.get("/aboutus/")
        self.assertEqual(response.status_code, 200)

    def test_about_us_page_by_name(self):
        response = self.client.get(reverse("aboutus"))
        self.assertEqual(response.status_code, 200)

    def test_about_us_page_content(self):
        response = self.client.get(reverse("aboutus"))
        self.assertContains(response, "About Us")

    def test_about_us_page_template(self):
        response = self.client.get(reverse("aboutus"))
        self.assertTemplateUsed((response, 'pages/aboutus.html'))
