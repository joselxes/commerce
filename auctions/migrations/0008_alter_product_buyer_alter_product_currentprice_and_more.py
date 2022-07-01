# Generated by Django 4.0.4 on 2022-06-24 16:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_rename_wishlist_itemslist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='buyer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='currentPrice',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='initialPrice',
            field=models.FloatField(),
        ),
    ]
