# Generated by Django 2.2.3 on 2019-09-23 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0011_auto_20190923_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='solution_key',
            field=models.SlugField(max_length=80, unique=True),
        ),
    ]