# Generated by Django 3.0.6 on 2023-06-03 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DasboardApp', '0002_auto_20230601_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='configname',
            name='user',
            field=models.CharField(default='Admin', max_length=300),
        ),
    ]
