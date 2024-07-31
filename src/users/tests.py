from django.test import TestCase
from .models import User 

class MyTestClass(TestCase):
    def setUpTestData():
       # Set up non-modified objects used by all test methods
       User.objects.create(username='Testing101', name='Adam Smith')

    def test_user_name_max_length(self):
        # Get a recipe object to test
        recipe = User.objects.get(id=1)
        # Get the metadata for the 'ingredients' field and use it to query its max_length
        max_length = recipe._meta.get_field('name').max_length
        # Compare the value to the expected result i.e. 120
        self.assertEqual(max_length, 120)


    def test_user_username_max_length(self):
        # Get a recipe object to test
        recipe = User.objects.get(id=1)
        # Get the metadata for the 'ingredients' field and use it to query its max_length
        max_length = recipe._meta.get_field('username').max_length
        # Compare the value to the expected result i.e. 120
        self.assertEqual(max_length, 120)
       
