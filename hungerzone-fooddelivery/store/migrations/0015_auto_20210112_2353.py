# Generated by Django 3.1.2 on 2021-01-12 20:53

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20210112_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=phone_field.models.PhoneField(help_text='Contact phone number', max_length=31),
        ),
    ]
