# Generated by Django 5.1.1 on 2024-10-07 08:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_reportactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportactive',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
