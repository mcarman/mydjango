# apps.links.views
from django.views.generic import ListView, DetailView
from django.views.generic import UpdateView, DeleteView
from django.views.generic.edit import CreateView, FormView
from apps.linkengine.models import Link, UserProfile, Vote
from django.contrib.auth import get_user_model
from apps.linkengine.forms import UserProfileForm, LinkForm, VoteForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect, get_object_or_404
import json
from django.http import HttpResponse


# list of links
class LinkListView(ListView):
    model = Link
    queryset = Link.with_votes.all()
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(LinkListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            voted = Vote.objects.filter(voter=self.request.user)
            links_in_page = [link.id for link in context["object_list"]]
            voted = voted.filter(link_id__in=links_in_page)
            voted = voted.values_list('link_id', flat=True)
            context["voted"] = voted
        return context




# Page to create a new link
class LinkCreateView(CreateView):
    model = Link
    form_class = LinkForm

    def form_valid(self, form):
        f = form.save(commit=False)
        f.rank_score = 0.0
        f.submitter = self.request.user
        f.save()

        return super(CreateView, self).form_valid(form)


# details on the link
class LinkDetailView(DetailView):
    model = Link


# edit and update ink
class LinkUpdateView(UpdateView):
    model = Link
    form_class = LinkForm


# Delete a link
class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy("home")


# vote and record votte status re said line
class JSONFormMixin(object):
    def create_response(self, vdict=dict(), valid_form=True):
        response = HttpResponse(json.dumps(vdict), content_type='application/json')
        response.status = 200 if valid_form else 500
        return response


class VoteFormBaseView(FormView):
    form_class = VoteForm

    def create_response(self, vdict=dict(), valid_form=True):
        response = HttpResponse(json.dumps(vdict))
        response.status = 200 if valid_form else 500
        return response

    def form_valid(self, form):
        link = get_object_or_404(Link, pk=form.data["link"])
        user = self.request.user
        prev_votes = Vote.objects.filter(voter=user, link=link)
        has_voted = (len(prev_votes) > 0)

        ret = {"success": 1}
        if not has_voted:
            # add vote
            v = Vote.objects.create(voter=user, link=link)
            ret["voteobj"] = v.id
        else:
            # delete vote
            prev_votes[0].delete()
            ret["unvoted"] = 1
        return self.create_response(ret, True)

    def form_invalid(self, form):
        ret = {"success": 0, "form_errors": form.errors}
        return self.create_response(ret, False)


# pass to voteview no need to change code in other parts
class VoteFormView(JSONFormMixin, VoteFormBaseView):
    pass
