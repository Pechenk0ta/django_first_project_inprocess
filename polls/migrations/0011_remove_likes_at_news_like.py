# Generated by Django 4.1.5 on 2023-02-01 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0010_likes_at_news"),
    ]

    operations = [
        migrations.RemoveField(model_name="likes_at_news", name="like",),
    ]
