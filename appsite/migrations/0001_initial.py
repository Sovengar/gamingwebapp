# Generated by Django 3.0.6 on 2020-05-18 16:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(default='default.jpg', upload_to='article_pics')),
                ('stock', models.IntegerField(default=0)),
                ('release_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]