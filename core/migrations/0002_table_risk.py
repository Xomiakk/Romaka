# Generated by Django 4.1.7 on 2023-04-04 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='risk',
            field=models.CharField(blank=True, default=None, max_length=8, null=True),
        ),
    ]
