# Generated by Django 3.2.15 on 2022-09-09 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_remove_role_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]