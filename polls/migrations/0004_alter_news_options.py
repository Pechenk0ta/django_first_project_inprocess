# Generated by Django 4.1.5 on 2023-01-25 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0003_coments_1"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="news",
            options={
                "ordering": ["created_at"],
                "verbose_name": "Новость",
                "verbose_name_plural": "Новости",
            },
        ),
    ]
