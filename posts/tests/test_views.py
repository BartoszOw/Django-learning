from django.test import TestCase, Client
from posts.models import Post, Author


class PostViewTest(TestCase):
    
    def setUp(self):
        self.author = Author.objects.create(nick='DA', email='d@d.pl')
        self.post = Post.objects.create(title='d', content='DAs', author=self.author)
        self.client = Client()

    def test_post_view(self):
        response = self.client.get('/posts/list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['posts']), 1)
        expected_link = f'<li><a href="/posts/list/{self.post.id}">{self.post.title}</a></li>'
        self.assertIn(expected_link, response.content.decode())


class AuthorViewTest(TestCase):
    
    def setUp(self):
        self.author = Author.objects.create(nick='xxx', email='x@x.pl')
        self.client = Client()

    def test_post_view(self):
        response = self.client.get('/posts/authors/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['authors']), 1)
        expected_link = f'<li><a href="/posts/authors/{self.author.id}">{self.author.nick} {self.author.email}</a></li>'
        self.assertIn(expected_link, response.content.decode())

