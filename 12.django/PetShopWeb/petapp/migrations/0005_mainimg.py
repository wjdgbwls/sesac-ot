# Generated by Django 3.2 on 2023-08-17 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0004_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='mainimgs/')),
            ],
        ),
    ]
