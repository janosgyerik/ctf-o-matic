# Generated by Django 2.2.3 on 2019-08-12 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0006_hint'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hint',
            old_name='hint',
            new_name='text',
        ),
    ]