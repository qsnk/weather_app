from django.contrib.auth.models import User
from django.test import TestCase
from weather.forms import WeatherForm, SignupForm, LoginForm


class WeatherFormTests(TestCase):
    def test_valid_form(self):
        form = WeatherForm(data={'city': 'Moscow'})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = WeatherForm(data={'city': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('city', form.errors)


class RegistrationFormTests(TestCase):
    def test_valid_form(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'securepassword',
            'password2': 'securepassword'
        }
        form = SignupForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_password_mismatch(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'securepassword',
            'password2': 'differentpassword'
        }
        form = SignupForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_form_missing_data(self):
        form_data = {
            'username': '',
            'email': 'testuser@example.com',
            'password1': 'securepassword',
            'password2': 'securepassword'
        }
        form = SignupForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)


class LoginFormTests(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'securepassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_valid_form(self):
        form_data = {
            'username': self.username,
            'password': self.password
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_wrong_password(self):
        form_data = {
            'username': self.username,
            'password': 'wrongpassword'
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.non_field_errors(), ['Invalid username or password'])

    def test_invalid_form_wrong_username(self):
        form_data = {
            'username': 'wrongusername',
            'password': self.password
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['__all__'], ['Invalid username or password'])

    def test_invalid_form_missing_data(self):
        form_data = {
            'username': '',
            'password': ''
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('password', form.errors)