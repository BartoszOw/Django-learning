from django.test import Client, TestCase
from posts.forms import PostForm, AuthorForm
from posts.models import Post, Author


class PostFormTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(nick='DAD',email='dad@dad.pl')
        
    def test_data_save_correct(self):
        data = {
            'title': 'Dadad', 
            'content': 'ADA',
            "created": "2024-05-20T17:34:16.387Z",
            "modified": "2024-05-20T17:34:16.387Z", 
            'author': self.author.id
                }
        self.assertEqual(len(Post.objects.all()), 0)
        form = PostForm(data=data)
        self.assertTrue(form.is_valid())
        p = form.save()
        self.assertIsInstance(p, Post)
        self.assertEqual(p.title, 'Dadad')
        self.assertEqual(p.content, 'ADA')
        self.assertEqual(p.author.id, 1)
        self.assertIsNotNone(p.id)
        

class AuthorFormTest(TestCase):

    def setUp(self):
        self.author1 = Author.objects.create(nick="AD", email='dad@dad.pl')

    def test_data_save_correct(self):
        data = {'nick': 'da', 'email': 'dada@dad.pl'}
        self.assertEqual(len(Author.objects.all()), 1)
        form = AuthorForm(data=data)
        self.assertTrue(form.is_valid())
        a = form.save()
        self.assertIsInstance(a, Author)
        self.assertEqual(a.nick, 'da')
        self.assertEqual(a.email, 'dada@dad.pl')
        self.assertIsNotNone(a.id)