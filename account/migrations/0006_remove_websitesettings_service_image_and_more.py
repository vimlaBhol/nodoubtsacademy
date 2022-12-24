# Generated by Django 4.1 on 2022-10-30 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_rename_website_settings_websitesettings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websitesettings',
            name='service_image',
        ),
        migrations.AddField(
            model_name='websitesettings',
            name='service_docs',
            field=models.FileField(blank=True, upload_to='servicedocs'),
        ),
    ]
