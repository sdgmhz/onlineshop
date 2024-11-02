from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class TestLoginSignUp(TestCase):
    username = 'myusername'
    email = 'myusername@gmail.com'

    def test_login_page_url(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)

    def test_login_page_url_name_content_template(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login")
        self.assertTemplateUsed(response, "account/login.html")

    def test_signup_page_url(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_page_url_name_content_template(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Signup")
        self.assertTemplateUsed(response, "account/signup.html")

    def test_signup_form(self):
        user = get_user_model().objects.create_user(
            self.username,
            self.email,
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)

