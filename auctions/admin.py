from django.contrib import admin
from .models import User,bid,product,comment,itemsList
# Register your models here.
# bid,product,comment,itemsList
admin.site.register(User)
admin.site.register(bid)
admin.site.register(product)
admin.site.register(comment)
admin.site.register(itemsList)