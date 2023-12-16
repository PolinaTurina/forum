from django.shortcuts import render
from django.urls import reverse_lazy

from forum_profile.forms import ProfileCreationForm
from forum_profile.models import Profile
from django.views.generic import CreateView



class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'forum_profile/create_profile.html'
    success_url = reverse_lazy('profile:create') 
