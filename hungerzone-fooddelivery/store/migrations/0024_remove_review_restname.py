# Generated by Django 3.1.2 on 2021-01-29 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_review_restname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='restname',
        ),
    ]