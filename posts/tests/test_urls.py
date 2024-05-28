from django.test import TestCase
from django.urls import resolve
from django.urls.exceptions import Resolver404
from posts.views import posts_details, author_details


class TestUrls(TestCase):

    def test_post_details_url(self):
        resolver = resolve('/posts/list/1')
        self.assertEqual(resolver.func, posts_details)
    def test_author_details_url(self):
        resolver = resolve('/posts/authors/1')
        self.assertEqual(resolver.func, author_details)
    def test_argument_or_404(self):
        with self.assertRaises(Resolver404):
            resolve('/post/list/a' or '/post/authors/a')