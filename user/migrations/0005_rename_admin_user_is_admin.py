# Generated by Django 4.1 on 2022-08-16 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='admin',
            new_name='Is_admin',
        ),
    ]