from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.urls import path

from .models import User, listing,question, product, getMonth, comment, itemsList, bid

Options=["Fashion","Toys","Electrics","Home"]
Items=[1,2,3,4,5]
count=1
def itemsCheck(auctionList,userA):
    wishItems=[]
    for i in auctionList:
        if itemsList.objects.filter(user=userA,products=i).all():
            wishItems.append([i,True])
        else:
            wishItems.append([i,False])
    return wishItems
def index(request):
    activeAuctions=product.objects.filter(state=True)
    isInWishList=[]
    username=request.user
    # print(username)
    try:
        user=User.objects.get(id=username.id)
        # print(user)
        return render(request, "auctions/index.html",{"activeAuctions":itemsCheck(activeAuctions,user)})
    except:
        return render(request, "auctions/index.html",{"activeAuctions":[]})

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

@login_required
def createList(request):
    return render(request, "auctions/createList.html",{ 
        "form": listing()
    })
# @login_required
def category(request):

    return render(request, "auctions/category.html",{"categoria":Options})
# @login_required
def listItems(request,department):
    activeAuctions=product.objects.filter( category = department)
    username=request.user
    user=User.objects.get(id=username.id)
    return render(request, "auctions/listItems.html",{
        "categoria":Options,"name":department,"activeAuctions":itemsCheck(activeAuctions,user)
})
# @login_required
def showItem(request,itemId):

    # if not(itemId in Items):
    #     return render(request, "auctions/error.html")

    username=request.user
    user=User.objects.get(id=username.id)
    prod=product.objects.get(id=itemId)
    print(prod.id,prod.description)    
    prodComments=comment.objects.filter(mssFor=prod)
    form=question()
    print(user!=prod.owner,user,prod.owner)
    wlist=itemsList.objects.get(user=user)
    # listaaa=wlist.products.all()
    # print(8888,  listaaa)
    return render(request, "auctions/showItem.html",{
        "prod":prod,
        "form":form,
        "comments":prodComments,
        "owner":user==prod.owner,
        "buyer":user==prod.buyer,
        "isInList":prod in wlist.products.all()
})
@login_required
def wishList(request):
    userName=request.user
    actualUser=User.objects.get(id=userName.id)
    try:
        items=itemsList.objects.get(user=actualUser)
    except:
        items=itemsList(user=actualUser)
        items.save()
    return render(request,"auctions/listItems.html",{"wishList":items.products.all(),"wishButton":True} )
@login_required
def postComment(request,itemId):
    if request.method == "POST":
        prod=product.objects.get(id=itemId)
        form=question(request.POST)
        if form.is_valid():
            tec=request.user
            userComment=User.objects.get(username=tec)
            newComment=form.cleaned_data["comment"]
            newRate=form.cleaned_data["rate"]     
            print(userComment,newRate,newComment)
            addedComment=comment(mssFrom=userComment,mssFor=prod,rate=int(newRate),content=newComment)
            addedComment.save()

            return HttpResponseRedirect(reverse("showItem",kwargs={'itemId':itemId}))

    # else:
        return render(request, "auctions/login.html")
@login_required
def addToList(request):
    if request.method == "POST":
        if True:
        # try:
            form=request.POST["productId"]
            userName=request.user
            user=User.objects.get(id=userName.id)
            userList= itemsList.objects.get(user=user)
            newProduct=product.objects.get(id=form)
            # print("addTolist- newProduct",newProduct)
            if userList is None:
                newList=itemsList(user=userName)
                newList.save()
                userList=newList
            checkProduct=itemsList.objects.filter(user=user,products=newProduct).all()
            # print("addTolist- checkProduct",checkProduct,form)
            if len(checkProduct) == 0:
                userList.products.add(newProduct)
            return HttpResponseRedirect(reverse("showItem",kwargs={"itemId":form}))
        # except:
        else:
            return HttpResponseRedirect(reverse("index"))            
    return HttpResponseRedirect(reverse("index"))
@login_required
def createAuction(request):
    if request.method == "POST":
        form=listing(request.POST)
        if form.is_valid():
            creator=request.user
            userCreator=User.objects.get(username=creator)
            title=form.cleaned_data["title"]
            initialPrice=form.cleaned_data["initialPrice"]
            # print(initialPrice,type(initialPrice),float(initialPrice),type(float(initialPrice)))
            category=form.cleaned_data["category"]
            description=form.cleaned_data["description"]
            newList=product(name=title, owner=userCreator ,initialPrice=initialPrice,currentPrice=initialPrice, description=description,category=category)
            newList.save()

            return HttpResponseRedirect(reverse("index"))

    return HttpResponseRedirect(reverse("index"))

@login_required
def postBid(request,itemId):
    if request.method == "POST":
        increase=float(request.POST["increase"])
        actualValue=float(request.POST["actualValue"])
        newPrice=increase+actualValue
        userName=request.user
        actualUser=User.objects.get(id=userName.id)

        prod=product.objects.get(id=itemId)
        # print(type(prod.currentPrice))
        if prod.currentPrice<newPrice:
            newBid=bid(user=actualUser,value=newPrice)
            newBid.save()
            prod.bids.add(newBid)
            prod.totalBids=prod.totalBids+1
            prod.currentPrice=newPrice
            prod.buyer=actualUser
            prod.save(update_fields=['totalBids','currentPrice','buyer'])
            print(prod.buyer)
            return HttpResponseRedirect(reverse("showItem",kwargs={'itemId':itemId}))


    return render(request,"auctions/index.html")

@login_required
def closeAuction(request,itemId):
    if request.method == "POST":
        username=request.user
        user=User.objects.get(id=username.id)
        if user==username:
            prod=product.objects.get(id=itemId)
            prod.state=False
            prod.save(update_fields=['state'])
            return HttpResponseRedirect(reverse("showItem",kwargs={'itemId':itemId}))


    return render(request,"auctions/index.html")

@login_required
def removeFromList(request):
    if request.method == "POST":
        if True:
        # try:
            form=request.POST["productId"]
            userName=request.user
            user=User.objects.get(id=userName.id)
            userList= itemsList.objects.get(user=user)
            newProduct=product.objects.get(id=form)
            # print("addTolist- newProduct",newProduct)
            if userList is None:
                newList=itemsList(user=userName)
                newList.save()
                userList=newList
            checkProduct=itemsList.objects.filter(user=user,products=newProduct).all()
            # print("addTolist- checkProduct",checkProduct,form)
            if len(checkProduct) != 0:
                print("ya esta en la lista")
                userList.products.remove(newProduct)
            return HttpResponseRedirect(reverse("showItem",kwargs={"itemId":form}))
        # except:
        else:
            return HttpResponseRedirect(reverse("index"))            
    return HttpResponseRedirect(reverse("index"))

"""
falta lo de las imagenes 
algo de admin
"""