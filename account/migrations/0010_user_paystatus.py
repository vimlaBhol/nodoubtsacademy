# Generated by Django 4.1 on 2022-11-11 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_user_userclass'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='paystatus',
            field=models.CharField(default='', max_length=200),
        ),
    ]