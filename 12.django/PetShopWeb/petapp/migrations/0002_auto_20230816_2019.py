# Generated by Django 3.2 on 2023-08-16 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phonenumber',
        ),
        migrations.AddField(
            model_name='user',
            name='user_number',
            field=models.TextField(default=''),
        ),
    ]
