# Generated by Django 4.1 on 2022-08-16 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_rename_is_admin_user_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
