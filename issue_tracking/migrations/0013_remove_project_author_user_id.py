# Generated by Django 4.0.2 on 2022-02-14 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracking', '0012_comment_author_user_id_issue_assigned_user_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='author_user_id',
        ),
    ]