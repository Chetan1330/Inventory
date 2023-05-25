# Generated by Django 3.0.7 on 2023-05-24 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0019_auto_20230524_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manufacturer',
            name='subcat_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manufacturer', to='inventory.Category'),
        ),
    ]
