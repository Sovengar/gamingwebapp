# Generated by Django 3.0.6 on 2021-06-21 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appsite', '0006_auto_20210615_1812'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opinion',
            options={'ordering': ['date_posted']},
        ),
    ]