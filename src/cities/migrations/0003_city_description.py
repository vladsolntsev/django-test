# Generated by Django 3.1.5 on 2021-01-27 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_auto_20210127_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='description',
            field=models.CharField(default='description', max_length=255),
        ),
    ]