# Generated by Django 3.0.7 on 2023-05-24 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0020_auto_20230524_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='class_name',
        ),
        migrations.AddField(
            model_name='category',
            name='class_name',
            field=models.ManyToManyField(to='inventory.Class1'),
        ),
    ]
