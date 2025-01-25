# Generated by Django 5.1.3 on 2025-01-25 16:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad_item', '0010_item_latitude_item_longitude'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='save_item',
            field=models.ManyToManyField(blank=True, null=True, related_name='save_product', to=settings.AUTH_USER_MODEL),
        ),
    ]
