# Generated by Django 3.0.6 on 2020-05-20 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsite', '0002_auto_20200518_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='new_article',
            field=models.BooleanField(default=True),
        ),
    ]
