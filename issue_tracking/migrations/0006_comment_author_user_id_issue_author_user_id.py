# Generated by Django 4.0.2 on 2022-02-06 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issue_tracking', '0005_project_author_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author_user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Comment', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='issue',
            name='author_user_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='Issue', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
