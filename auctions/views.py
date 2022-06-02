from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls import path

from .models import User, listing

Options=["Fashion","Toys","Electrics","Home"]
Items=[1,2,3,4,5]
def index(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def createList(request):
    return render(request, "auctions/createList.html",{ 
        "form": listing
    })

def category(request):
    return render(request, "auctions/category.html",{"categoria":Options})

def listItems(request,department):
    return render(request, "auctions/listItems.html",{
        "categoria":Options,"name":department,"items":Items
})
def showItem(request,itemId):

    if not(itemId in Items):
        return render(request, "auctions/error.html") 
    return render(request, "auctions/showItem.html",{
        "categoria":Options,"name":Options[0],"item":1

})