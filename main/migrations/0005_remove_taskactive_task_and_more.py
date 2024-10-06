# Generated by Django 5.1.1 on 2024-10-06 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_date_created_reportactive_date_reported_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskactive',
            name='task',
        ),
        migrations.AddField(
            model_name='taskactive',
            name='benefits_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='taskactive',
            name='description',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskactive',
            name='location',
            field=models.CharField(default='Ashgabat', max_length=255),
        ),
        migrations.AddField(
            model_name='taskactive',
            name='title',
            field=models.CharField(default='w', max_length=255),
            preserve_default=False,
        ),
    ]
