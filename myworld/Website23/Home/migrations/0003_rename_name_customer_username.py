# Generated by Django 4.1.7 on 2023-05-29 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_rename_user_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='username',
        ),
    ]