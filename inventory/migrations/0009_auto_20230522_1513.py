# Generated by Django 3.0.7 on 2023-05-22 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20230522_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='Shortdesc',
            field=models.CharField(default=False, max_length=150),
        ),
    ]
