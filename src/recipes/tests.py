from django.test import TestCase
from .models import Recipe 

class MyTestClass(TestCase):
    def setUpTestData():
       # Set up non-modified objects used by all test methods
       Recipe.objects.create(name='Ravoili', cooking_time='10', ingredients='ravioli, sauce, cheese', description='this is a traditional Italian dish')

    def test_recipe_name(self):
       # Get a recipe object to test
       recipe = Recipe.objects.get(id=1)

       # Get the metadata for the 'name' field and use it to query its data
       field_label = recipe._meta.get_field('name').verbose_name

       # Compare the value to the expected result
       self.assertEqual(field_label, 'name')

    def test_ingredients_max_length(self):
           # Get a recipe object to test
           recipe = Recipe.objects.get(id=1)
           # Get the metadata for the 'ingredients' field and use it to query its max_length
           max_length = recipe._meta.get_field('ingredients').max_length
           # Compare the value to the expected result
           self.assertEqual(max_length, 225)

    def test_cooking_time_is_integer(self):
        recipe = Recipe.objects.get(id=1)
        cooking_time = recipe.cooking_time
        self.assertIs(type(cooking_time), int, 'cooking_time is not a number')

    def test_recipe_description(self):
       recipe = Recipe.objects.get(id=1)
       field_label = recipe._meta.get_field('description').verbose_name
       self.assertEqual(field_label, 'description')
