# Generated by Django 4.2 on 2023-05-24 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_tokens_accesstoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_officer',
            field=models.BooleanField(default=False),
        ),
    ]
