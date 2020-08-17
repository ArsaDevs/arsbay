# Generated by Django 3.1 on 2020-08-15 19:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_remove_auction_current_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='watchlist', to=settings.AUTH_USER_MODEL),
        ),
    ]