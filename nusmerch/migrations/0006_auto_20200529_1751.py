# Generated by Django 3.0.6 on 2020-05-29 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nusmerch', '0005_auto_20200529_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='user_faculty',
            new_name='faculty',
        ),
    ]
