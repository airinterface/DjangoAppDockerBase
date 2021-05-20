# Generated by Django 3.2.3 on 2021-05-20 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0002_story_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='story',
            name='img',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='story',
            name='data',
            field=models.JSONField(default={}),
        ),
    ]
