# apps.links.views
from django.views.generic import ListView, DetailView
from django.views.generic import UpdateView, DeleteView
from django.views.generic.edit import CreateView, FormView
from apps.linkengine.models import Link, UserProfile, Vote
from django.contrib.auth import get_user_model
from apps.linkengine.forms import UserProfileForm, LinkForm, VoteForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect, get_object_or_404


# list of links
class LinkListView(ListView):
    model = Link
    queryset = Link.with_votes.all()
    paginate_by = 3


# Display bio/details of a user
class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "user_detail.html"

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user


# edit the bio
class UserProfileEditView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "edit_profile.html"

    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        return reverse("profile", kwargs={'slug': self.request.user})


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


# vote and record votte status re said link
class VoteFormView(FormView):
    form_class = VoteForm

    def form_valid(self, form):
        link = get_object_or_404(Link, pk=form.data["link"])
        user = self.request.user
        prev_votes = Vote.objects.filter(voter=user, link=link)
        has_voted = (prev_votes.count() > 0)

        if not has_voted:
            # add vote
            Vote.objects.create(voter=user, link=link)
            print("voted")
        else:
            # delete vote
            prev_votes[0].delete()
            print("unvoted")

        return redirect("home")

    def form_invalid(self, form):
        print("invalid")
        return redirect("home")
