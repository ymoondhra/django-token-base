import json
from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import CustomUser
from .serializers import UserSerializer


class UserModelTestCase(TestCase):
    # Only functions that start with lowercase "test" are automatically executed.
    # The objects created in a "test" function do not persist after the function ends
    # They are executed in alphabetical order

    # setUp is called before every test
    def setUp(self):
        self.UserModel = get_user_model()
        self.username1 = "apple"
        self.user1 = self.UserModel.objects.create(
          username=self.username1,
          email=self.username1 + "@" + self.username1 + ".com",
          password="ZetaBeta005")
        self.user_count = 1

    # tearDown is called after every test
    def tearDown(self):
        pass

# MODEL
    def test_user_model(self):
        self.assertEquals(self.UserModel, CustomUser)  # the project is using the CustomUser model

    def test_user_created(self):
        custom_user = self.UserModel.objects.filter(username=self.username1)
        self.assertEqual(custom_user.count(), 1)
  
    def test_user_str(self):  # tests the __str__ method
        self.assertTrue(self.user1, self.username1)

# SERIALIZER
    def test_user_serializer_expected_fields(self):
        serializer = UserSerializer(instance=self.user1)
        data = serializer.data
        self.assertCountEqual(data.keys(), ['email', 'username'])

    def test_user_serializer_field_content(self):
        serializer = UserSerializer(instance=self.user1)
        data = serializer.data
        self.assertEqual(data['username'], self.username1)
        self.assertEqual(data['email'], self.username1 + "@" + self.username1 + ".com")

# VIEWS
    def test_user_view_userlistview(self):
        username2 = "banana"
        self.UserModel.objects.create(
            username=username2,
            email=username2 + "@" + username2 + ".net",
            password="BetaZeta500")
        response = self.client.get('/api/v1/users/')
        self.assertEquals(response.status_code, 200)
        response_user_count = len(json.loads(response.content))
        self.assertEquals(response_user_count, self.user_count + 1)
        # + 1 because we created user in this function, but that user will disappear after the function returns

    def test_user_view_userdetail(self):
        response = self.client.get('/api/v1/users/' + str(self.user1.id))
        self.assertEquals(response.status_code, 200)
        response_username = json.loads(response.content)['username']
        self.assertEquals(response_username, self.username1)
