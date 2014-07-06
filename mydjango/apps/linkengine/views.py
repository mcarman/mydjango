# apps.links.views
from django.views.generic import ListView, DetailView
from django.views.generic import UpdateView, DeleteView
from django.views.generic.edit import CreateView
from models import Link, UserProfile
from django.contrib.auth import get_user_model
from forms import UserProfileForm, LinkForm
from django.core.urlresolvers import reverse, reverse_lazy


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
