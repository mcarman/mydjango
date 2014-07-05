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

    # def test_create_tag(self):
    #     # Create the tag
    #     tag = Tag()

    #     # Add attributes
    #     tag.name = 'python'
    #     tag.description = 'The Python programming language'
    #     tag.slug = 'python'

    #     # Save it
    #     tag.save()

    #     # Check we can find it
    #     all_tags = Tag.objects.all()
    #     self.assertEquals(len(all_tags), 1)
    #     only_tag = all_tags[0]
    #     self.assertEquals(only_tag, tag)

    #     # Check attributes
    #     self.assertEquals(only_tag.name, 'python')
    #     self.assertEquals(only_tag.description, 'The Python programming language')
    #     self.assertEquals(only_tag.slug, 'python')

    def test_create_link(self):
        # Create the link
        link = Link()
        title = 'amazon'
        submitter = 'bobsmith'
        sub_date = timezone.now()
        rank_score = '1'
        url = 'http://www.amazon.com/?tag=tais2-desktop-20'
        description = 'Amazon shopping site - desktop'
        link.save()

        # Check we can find it
        all_links = Link.objects.all()
        self.assertEquals(len(all_links), 1)
        only_link = all_links[0]
        self.assertEquals(only_link, link)

        # Check attributes
        self.assertEquals(only_link.title, 'Amazon')
        self.assertEquals(only_link.submitter, 'bobsmith')
        self.assertEquals(only_link.description, 'Amazon shopping site - desktop')
        self.assertEquals(only_link.rank_score, '1')
        self.assertEquals(only_link.url, 'http://www.amazon.com/?tag=tais2-desktop-20')
        self.assertEquals(only_link.sub_date.day, link.sub_date.day)
        self.assertEquals(only_link.sub_date.month, link.sub_date.month)
        self.assertEquals(only_link.pub_date.year, link.sub_date.year)
        self.assertEquals(only_link.pub_date.hour, link.sub_date.hour)
        self.assertEquals(only_link.pub_date.minute, link.sub_date.minute)
        self.assertEquals(only_link.pub_date.second, link.sub_date.second)

        # # Check tags
        # post_tags = only_post.tags.all()
        # self.assertEquals(len(post_tags), 1)
        # only_post_tag = post_tags[0]
        # self.assertEquals(only_post_tag, tag)
        # self.assertEquals(only_post_tag.name, 'python')
        # self.assertEquals(only_post_tag.description, 'The Python programming language')


