# Generated by Django 3.1.2 on 2020-10-29 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_auto_20201029_0214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='profile_det',
        ),
    ]
