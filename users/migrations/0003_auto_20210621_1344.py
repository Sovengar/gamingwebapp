# Generated by Django 3.0.6 on 2021-06-21 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210611_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='rating',
            field=models.IntegerField(default=3),
        ),
    ]