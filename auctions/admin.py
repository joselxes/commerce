from django.contrib import admin
from .models import product,User,comment,itemsList
# Register your models here.

admin.site.register(product)
admin.site.register(comment)
admin.site.register(User)
admin.site.register(itemsList)