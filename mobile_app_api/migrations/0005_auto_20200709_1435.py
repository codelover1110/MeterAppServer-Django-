# Generated by Django 2.1.15 on 2020-07-09 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_app_api', '0004_consumption'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadata',
            name='latitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='metadata',
            name='longtitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]