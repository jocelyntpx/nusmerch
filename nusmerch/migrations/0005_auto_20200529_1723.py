# Generated by Django 3.0.6 on 2020-05-29 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nusmerch', '0004_movieinfo_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('user_number', models.IntegerField(max_length=8)),
                ('user_email', models.CharField(max_length=200)),
                ('user_faculty', models.CharField(max_length=50)),
                ('user_password', models.CharField(max_length=50)),
                ('user_repeatpass', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='MovieInfo',
        ),
        migrations.DeleteModel(
            name='MovieInfo_Test',
        ),
    ]
