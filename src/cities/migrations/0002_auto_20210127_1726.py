# Generated by Django 3.1.5 on 2021-01-27 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='state',
            new_name='country',
        ),
    ]
