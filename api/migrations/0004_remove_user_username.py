# Generated by Django 5.1 on 2024-08-28 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_options_alter_user_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
