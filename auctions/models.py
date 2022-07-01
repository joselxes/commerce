from random import choices
from unicodedata import category
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django import forms
from django.utils import timezone
import datetime
meses={ "1":"Enero", "2":"Febrero", "3":"Marzo", "4":"Abril", "5":"Mayo", "6":"Junio", "7":"Julio", "8":"Agosto", "9":"Septiembre", "10":"Octubre", "11":"Noviembre", "12":"Diciembre",}
categoryOptions=(("Fashion","Fashion"),("Toys","Toys"),("Electrics","Electrics"),("Home","Home"),)

def getMonth(monthNumber):
    return meses[str(monthNumber)]

def getDateAsList():
    today=datetime.datetime.now()
    todayList=[today.year,today.month,today.day, today.hour, today.minute,]
    return todayList
class User(AbstractUser):
    pass

class newBid(forms.Form):
    increase=forms.IntegerField(label="Start at", 
        widget= forms.NumberInput(attrs={'class':'some_class','id':'some_id','placeholder':'Starter Price'}))

class question(forms.Form):
    
    comment=forms.CharField(label="comment", widget=forms.Textarea(attrs={'rows':'3','cols':'30',
    'class':'form-control','id':'some_id','placeholder':'Ask o make an opinion related to the product'}))
    rate=forms.IntegerField(label="rate", min_value=1, max_value=5 ,widget=forms.NumberInput( attrs={ 'class':'some_class','id':'some_id','placeholder':'Rate product'} ) )


class listing(forms.Form):

    title=forms.CharField(label="Title",
      widget= forms.TextInput(attrs={'class':'form-control','id':'some_id','placeholder':'Titlee'}))

    initialPrice=forms.FloatField(label="Start at", min_value=0,
        widget= forms.NumberInput(attrs={'class':'some_class','id':'some_id','placeholder':'Starter Price'}))

#     productImage=forms.ImageField(label="Imagen",
# widget= forms.FileInput(attrs={'class':'some_class','id':'some_id'}))

    category=forms.ChoiceField(label="Category", choices=categoryOptions,
        widget= forms.Select(attrs={'class':'form-control','id':'some_id','placeholder':'Category','width':'10%'}))    
    
    description=forms.CharField(label="Description", widget=forms.Textarea(attrs={'rows':'15','cols':'90',
    'class':'form-control','id':'some_id','placeholder':'Description'}))
class bid(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    value=models.FloatField(blank=False)
    def __str__(self):
        return f"{self.user} {self.value}"
  
class product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,related_name='seller')
    initialPrice = models.FloatField()    
    currentPrice=models.FloatField(blank=True)
    description = models.CharField(max_length=50)
    state=models.BooleanField(default=True)
    # publishDate = models.DateField(default=datetime.date.today())
    publishDate = models.DateField(default=timezone.now)
    category = models.CharField(max_length=25,choices=categoryOptions)
    totalBids=models.IntegerField(default=0)
    buyer=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE, related_name='buyer')
    bids=models.ManyToManyField(bid,related_name="values")    
    def __str__(self):
        return f"{self.name} {self.id}"

class  comment(models.Model):
    mssFrom=models.ForeignKey(User,default="",blank=False,on_delete=models.CASCADE,related_name="comentator")
    mssFor=models.ForeignKey(product,on_delete=models.CASCADE, related_name="product")
    date=models.DateField(default=timezone.now)
    rate=models.IntegerField()
    content=models.CharField(max_length=100)
    def __str__(self):
        return f"rate:{self.rate}, date:{self.date}, content:{self.content} "
# comment(mssFrom=User,mssFor=product,rate=3,content=strs)

class itemsList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, primary_key=True)
    products=models.ManyToManyField(product, blank=True)
    def __str__(self):
        return f"{self.user} "
"""
from auctions.models import *
pa1=productDetails(productTitle = "lavadora", initialPrice = 12, productOwner = "userA",  categoryProduct = "electronic",  productDescription = "aaaaaaaaaaaaaa")
pa1.save()
pa1
users=User.objects.all()
users
user1=User.objects.first()
user1
pa2=productDetails(productTitle = "play4", initialPrice = 200, productOwner = user1,  categoryProduct = "electronic",  productDescription = "Play play play")
pa2.save()
pa2
auction1=auctionProduct(productCurrentState=True, productCurrentPrice=123,sellingProduct=pa2,publishDate=getDateAsList(),bids=12,buyer=user1)
auction1.save()
auction1


""" 