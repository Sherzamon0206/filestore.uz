# Generated by Django 3.2.6 on 2022-04-10 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0004_auto_20220410_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search_word',
            name='count_search',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
    ]
