# Generated by Django 5.1.4 on 2024-12-08 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareme', '0002_user42_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='user42',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]