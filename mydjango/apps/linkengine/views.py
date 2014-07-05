# apps.links.views
from django.views.generic import ListView
from models import Link, Vote


# list of links
class LinkListView(ListView):
    model = Link
    queryset = Link.with_votes.all()
    paginate_by = 3
