# Generated by Django 4.1 on 2022-10-01 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_name_user_firstname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contact',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='usertype',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='firstname',
            field=models.CharField(default='', max_length=200),
        ),
    ]