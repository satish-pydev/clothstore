# Generated by Django 3.1.6 on 2021-06-25 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='lname',
        ),
    ]
