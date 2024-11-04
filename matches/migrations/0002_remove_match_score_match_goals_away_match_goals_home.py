# Generated by Django 5.1.2 on 2024-11-04 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='score',
        ),
        migrations.AddField(
            model_name='match',
            name='goals_away',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='goals_home',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]