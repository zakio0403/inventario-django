# Generated by Django 3.1.14 on 2022-03-01 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20220301_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='softwarerequirements',
            name='observation',
        ),
        migrations.AddField(
            model_name='apprequirements',
            name='observation',
            field=models.TextField(blank=True, max_length=500, verbose_name='Observaciones'),
        ),
        migrations.AddField(
            model_name='bdrequirements',
            name='observation',
            field=models.TextField(blank=True, max_length=500, verbose_name='Observaciones'),
        ),
    ]
