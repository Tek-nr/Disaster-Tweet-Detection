# Generated by Django 4.1.9 on 2023-06-01 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweety', '0009_remove_tweety_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweety',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
