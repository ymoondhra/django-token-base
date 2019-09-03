import json
from rest_framework.test import APITestCase


# These test cases ensure the success of the functionality of the endpoints defined in urls.py
class ApiTestCase(APITestCase):
    # only functions that start with lowercase "test" are automatically executed.
    # They are executed in alphabetical order

    # setUp is called before every test
    def setUp(self):
        self.general_credentials = {'username': 'apple', 'password': 'myapple29'}
        self.email = 'apple@apple.com'

        # test signup endpoint
        # this code must be in setUp so that the CustomUser object is saved to the database
        signup_credentials = {'username': self.general_credentials['username'],
                              'email': self.email,
                              'password1': self.general_credentials['password'],
                              'password2': self.general_credentials['password']}
        response = self.client.post('/api/v1/rest-auth/registration/', signup_credentials, format='json')
        self.assertContains(response, text='key', status_code=201)
        self.key = json.loads(response.content)['key']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.key))

    # tearDown is called after every test
    def tearDown(self):
        pass

# URLS
    def test_api_users_urls(self):
        pass  # done in users/tests.py

    # the account created in this function does not persist after this function ends
    def test_api_signup_without_email(self):
        signup_credentials = {'username': self.general_credentials['username'] + '2',
                              'password1': self.general_credentials['password'],
                              'password2': self.general_credentials['password']}
        response = self.client.post('/api/v1/rest-auth/registration/', signup_credentials, format='json')
        self.assertContains(response, text='key', status_code=201)

    # Not Supported: Email verification
    # def test_api_verify_email(self):

    def test_api_password_reset(self):
        email = {'email': self.email}
        response = self.client.post('/api/v1/rest-auth/password/reset/', email, format='json')
        self.assertContains(response, text='Password reset e-mail has been sent.', status_code=200)

    # Not Supported: Password reset confirmation
    # def test_api_password_reset_confirm(self):

    def test_api_login(self):
        login_credentials = {'username': self.general_credentials['username'],
                             'password': self.general_credentials['password']}
        response = self.client.post('/api/v1/rest-auth/login/', login_credentials, format='json')
        self.assertContains(response, text=self.key, status_code=200)

    def test_api_user(self):
        response = self.client.get('/api/v1/rest-auth/user/')
        for key in ('pk', 'username', 'email', 'first_name', 'last_name'):
            self.assertContains(response, text=key, status_code=200)

    def test_api_change_password(self):
        password = {'old_password': self.general_credentials['password'],
                    'new_password1': self.general_credentials['password'] + '2',
                    'new_password2': self.general_credentials['password'] + '2'}
        response = self.client.post('/api/v1/rest-auth/password/change/', password, format='json')
        self.assertContains(response, text='New password has been saved.', status_code=200)

    def test_api_logout(self):
        response = self.client.post('/api/v1/rest-auth/logout/')
        self.assertContains(response, text='Successfully logged out.', status_code=200)