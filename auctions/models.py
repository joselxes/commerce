from random import choices
from unicodedata import category
from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms


class User(AbstractUser):
    pass

class listing(forms.Form):
    Options=(
        ("Fashion","Fashion"),
        ("Toys","Toys"),
        ("Electrics","Electrics"),
        ("Home","Home"),
        )
    title=forms.CharField(label="Title",
      widget= forms.TextInput(attrs={'class':'form-control','id':'some_id','placeholder':'Title'}))

    # inPrice=MoneyField(label="Start at",max_digits=14, decimal_places=2,default_currency='USD',
        # widget= forms.NumberInput(attrs={'class':'form-control','id':'some_id','placeholder':'Starter Price'}))

    inPrice=forms.IntegerField(label="Start at", min_value=0,
        widget= forms.NumberInput(attrs={'class':'some_class','id':'some_id','placeholder':'Starter Price'}))

    image=forms.CharField(label="Imagen",
        widget= forms.TextInput(attrs={'class':'some_class','id':'some_id','placeholder':'Imagen'}))

    category=forms.ChoiceField(label="Category", choices=Options,
        widget= forms.Select(attrs={'class':'form-control','id':'some_id','placeholder':'Category','width':'10%'}))    
    
    description=forms.CharField(label="Description", widget=forms.Textarea(attrs={'rows':'15','cols':'90',
    'class':'form-control','id':'some_id','placeholder':'Description'}))



# class listing(forms.Form):
#     Options=(
#         ("Fashion","Fashion"),
#         ("Toys","Toys"),
#         ("Electrics","Electrics"),
#         ("Home","Home"),
#         )
#     title=forms.CharField(label="Title",
#       widget= forms.TextInput(attrs={'class':'form-control','id':'some_id','placeholder':'Title'}))

#     # inPrice=MoneyField(label="Start at",max_digits=14, decimal_places=2,default_currency='USD',
#         # widget= forms.NumberInput(attrs={'class':'form-control','id':'some_id','placeholder':'Starter Price'}))

#     initialPrice=forms.IntegerField(label="Start at", min_value=0,
#         widget= forms.NumberInput(attrs={'class':'some_class','id':'some_id','placeholder':'Starter Price'}))

#     sellPrice=forms.IntegerField(min_value=0)

#     seller=forms.CharField(min_value=0)

#     id=forms.CharField(min_value=0)

#     image=forms.CharField(label="Imagen",
#         widget= forms.TextInput(attrs={'class':'some_class','id':'some_id','placeholder':'Imagen'}))

#     category=forms.ChoiceField(label="Category", choices=Options,
#         widget= forms.Select(attrs={'class':'form-control','id':'some_id','placeholder':'Category','width':'10%'}))    
    
#     description=forms.CharField(label="Description", widget=forms.Textarea(attrs={'rows':'15','cols':'90',
#     'class':'form-control','id':'some_id','placeholder':'Description'}))
