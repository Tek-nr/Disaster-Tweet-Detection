# Generated by Django 4.2.1 on 2023-05-31 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweety', '0004_remove_profile_password_profile_date_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweety',
            name='dates',
        ),
    ]
