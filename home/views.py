from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from summary.models import Summary


@login_required
def home_page(request):
    qs = Summary.objects.all()

    context = {'summary_list': qs}

    return render(request, "home/index.html", context)