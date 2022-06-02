from django import forms



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
        widget= forms.Select(attrs={'class':'form-control','id':'some_id','placeholder':'Category'}))    
    
    description=forms.CharField(label="Description", widget=forms.Textarea(attrs={'rows':'15','cols':'90',
    'class':'form-control','id':'some_id','placeholder':'Description'}))
     