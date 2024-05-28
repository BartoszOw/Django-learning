from django.test import TestCase, Client
from posts.models import Post, Author


class PostModelTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(nick='DA', email='d@d.pl')
        Post.objects.create(title='d', content='DAs', author=self.author)
        Post.objects.create(title='v', content='xx', author=self.author)

    def test_post_str(self):
        p1 = Post.objects.get(title='d')
        p2 = Post.objects.get(content='xx')

        self.assertEqual(str(p1), f'id:{p1.id}, title:d, content:DAs, author:{p1.author.id}')
        self.assertEqual(str(p2), f'id:{p2.id}, title:v, content:xx, author:{p2.author.id}')


class AuthorModelTest(TestCase):

    def setUp(self):
        Author.objects.create(nick='DA', email='d@d.pl')

    def test_author_str(self):
        a1 = Author.objects.get(nick='DA')

        self.assertEqual(str(a1), 'DA, d@d.pl')
    

