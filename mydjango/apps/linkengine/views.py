# apps.links.views
from django.views.generic import ListView
from models import Link, Vote


# list of links
class LinkListView(ListView):
    model = Link
