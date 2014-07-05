# apps.links.tests
from django.test import TestCase, LiveServerTestCase, Client
from django.utils import timezone
from apps.links.models import Link, Vote
from django.contrib.sites.models import Site
from django.contrib.auth.models import User


class PostTest(TestCase):
    def test_create_vote(self):
        # Create the Vote
        vote = Vote()

        # Add attributes
        vote.voter = 'bobsmith'
        vote.link = 'Amazon'

        # Save it
        vote.save()

        # Check we can find it
        all_categories = vote.objects.all()
        self.assertEquals(len(all_categories), 1)
        only_category = all_categories[0]
        self.assertEquals(only_category, category)

        # Check attributes
        self.assertEquals(only_vote.voter, 'bobsmith')
        self.assertEquals(only_vote.link, 'Amazon')

    def test_create_tag(self):
        # Create the tag
        tag = Tag()

        # Add attributes
        tag.name = 'python'
        tag.description = 'The Python programming language'
        tag.slug = 'python'

        # Save it
        tag.save()

        # Check we can find it
        all_tags = Tag.objects.all()
        self.assertEquals(len(all_tags), 1)
        only_tag = all_tags[0]
        self.assertEquals(only_tag, tag)

        # Check attributes
        self.assertEquals(only_tag.name, 'python')
        self.assertEquals(only_tag.description, 'The Python programming language')
        self.assertEquals(only_tag.slug, 'python')

    def test_create_post(self):
        # Create the category
        category = Category()
        category.name = 'python'
        category.description = 'The Python programming language'
        category.save()

        # Create the tag
        tag = Tag()
        tag.name = 'python'
        tag.description = 'The Python programming language'
        tag.save()

        # Create the author
        author = User.objects.create_user('testuser', 'user@example.com', 'password')
        author.save()

        # Create the site
        site = Site()
        site.name = 'example.com'
        site.domain = 'example.com'
        site.save()

        # Create the post
        post = Post()

        # Set the attributes
        post.title = 'My first post'
        post.text = 'This is my first blog post'
        post.slug = 'my-first-post'
        post.pub_date = timezone.now()
        post.author = author
        post.site = site
        post.category = category

        # Save it
        post.save()

        # Add the tag
        post.tags.add(tag)
        post.save()

        # Check we can find it
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)
        only_post = all_posts[0]
        self.assertEquals(only_post, post)

        # Check attributes
        self.assertEquals(only_post.title, 'My first post')
        self.assertEquals(only_post.text, 'This is my first blog post')
        self.assertEquals(only_post.slug, 'my-first-post')
        self.assertEquals(only_post.site.name, 'example.com')
        self.assertEquals(only_post.site.domain, 'example.com')
        self.assertEquals(only_post.pub_date.day, post.pub_date.day)
        self.assertEquals(only_post.pub_date.month, post.pub_date.month)
        self.assertEquals(only_post.pub_date.year, post.pub_date.year)
        self.assertEquals(only_post.pub_date.hour, post.pub_date.hour)
        self.assertEquals(only_post.pub_date.minute, post.pub_date.minute)
        self.assertEquals(only_post.pub_date.second, post.pub_date.second)
        self.assertEquals(only_post.author.username, 'testuser')
        self.assertEquals(only_post.author.email, 'user@example.com')
        self.assertEquals(only_post.category.name, 'python')
        self.assertEquals(only_post.category.description, 'The Python programming language')

        # Check tags
        post_tags = only_post.tags.all()
        self.assertEquals(len(post_tags), 1)
        only_post_tag = post_tags[0]
        self.assertEquals(only_post_tag, tag)
        self.assertEquals(only_post_tag.name, 'python')
        self.assertEquals(only_post_tag.description, 'The Python programming language')


class BaseAcceptanceTest(LiveServerTestCase):
    def setUp(self):
        self.client = Client()


class AdminTest(BaseAcceptanceTest):
    fixtures = ['users.json']

    def test_create_link(self):
        # Create the link
        link = Link()
        title = 'amazon'
        submitter = 'bobsmith'
        submitted_on = ''
        rank_score = '1.2'
        url = 'http://www.amazon.com/?tag=tais2-desktop-20'
        description = 'Amazon shopping site'
        link.save()

        # # Create the tag
        # tag = Tag()
        # tag.name = 'python'
        # tag.description = 'The Python programming language'
        # tag.save()

        # Log in
        self.client.login(username='bobsmith', password="password")

        # Check response code
        response = self.client.get('/admin/links/link/add/')
        self.assertEquals(response.status_code, 200)

        # Create the new post
        response = self.client.post('/admin/links/link/add/', {
            title = 'amazon'
            submitter = models.ForeignKey(User)
            submitted_on = models.DateTimeField(auto_now_add=True)
            rank_score = '1.2'
            url = 'http://www.amazon.com/?tag=tais2-desktop-20'
            description = 'Amazon shopping site'
        },
            follow=True
        )
        self.assertEquals(response.status_code, 200)

        # Check added successfully
        self.assertTrue('added successfully' in response.content)

        # Check new post now in database
        all_posts = Post.objects.all()
        self.assertEquals(len(all_posts), 1)
