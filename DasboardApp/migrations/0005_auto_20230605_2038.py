# Generated by Django 3.0.6 on 2023-06-05 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DasboardApp', '0004_auto_20230603_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='Configname',
            field=models.CharField(blank=True, max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='Reservedby',
            field=models.CharField(blank=True, max_length=700, null=True),
        ),
    ]
