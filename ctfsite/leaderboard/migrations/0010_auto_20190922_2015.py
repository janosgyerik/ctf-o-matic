# Generated by Django 2.2.3 on 2019-09-22 18:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leaderboard', '0009_server'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaderboard.Server')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='userserver',
            constraint=models.UniqueConstraint(fields=('user',), name='uk_user'),
        ),
    ]
