# Generated by Django 3.0.6 on 2021-06-11 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_teaser_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='teaser_content',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
