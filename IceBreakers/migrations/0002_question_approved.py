# Generated by Django 4.2.11 on 2024-04-22 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IceBreakers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
