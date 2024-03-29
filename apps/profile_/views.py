from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.profile_.models import Profile
from apps.profile_.forms import ProfileForm


class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile/profile_form.html'
    success_url = reverse_lazy('profile_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile/profile_form.html'
    success_url = reverse_lazy('profile_list')


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'profile/profile_confirm_delete.html'
    success_url = reverse_lazy('profile_list')


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile/profile_detail.html'


class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'profile/profile_list.html'
