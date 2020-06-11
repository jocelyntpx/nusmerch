# Generated by Django 3.0.6 on 2020-06-11 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nusmerch', '0008_auto_20200611_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField()),
                ('organisation', models.CharField(max_length=200, null=True)),
                ('form', models.URLField()),
            ],
        ),
    ]
