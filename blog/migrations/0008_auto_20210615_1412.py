# Generated by Django 3.0.6 on 2021-06-15 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210611_1530'),
        ('blog', '0007_auto_20210611_1639'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together={('author', 'post')},
        ),
    ]
