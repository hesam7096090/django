# Generated by Django 5.1.3 on 2025-01-14 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad_item', '0004_alter_item_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]