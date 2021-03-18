# Generated by Django 3.1.2 on 2021-02-01 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_auto_20210129_2033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='rateCount',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='favorite', to='store.Customer'),
        ),
    ]
