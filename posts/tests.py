"""This module does blah blah."""

from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.

class PostModelTest(TestCase):
    """This class does blah blah."""

    def setUp(self):
        Post.objects.create(text='just a test')

    def test_text_content(self):
        """This class does blah blah."""

        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'just a test')


class HomePageViewTest(TestCase):
    """This class does blah blah."""

    def setUp(self):
        Post.objects.create(test='this is another test')

    def test_view_url_exists_at_proper_location(self):
        """This method does blah blah."""
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

