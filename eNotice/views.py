from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
def index(request):
    if not request.user.is_authenticated:
        return render(request, "home.html")
    else:
        return HttpResponseRedirect(reverse("notices:home"))