from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def profile_list(request):
    return render(request, "profile_page/profile_list.html")