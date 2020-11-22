from django.contrib.auth.models import User
from django.views.generic.detail import DetailView


class ProfileView(DetailView):
    context_object_name = 'profile_user'
    model = User
    template_name = 'profile_page/profile_list.html'