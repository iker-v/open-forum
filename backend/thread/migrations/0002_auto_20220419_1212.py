# Generated by Django 3.2.6 on 2022-04-19 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='downvotes',
            old_name='post',
            new_name='thread',
        ),
        migrations.RenameField(
            model_name='upvotes',
            old_name='post',
            new_name='thread',
        ),
    ]
