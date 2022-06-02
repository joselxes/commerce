from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from auctions.models import listing

# from .models import User, listing


def index(request):
    a=listing
    return render(request, "categ/index.html",{'list':a})

