# Generated by Django 3.2.15 on 2022-09-09 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20220908_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]