# Generated by Django 3.0.6 on 2021-06-11 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='genre',
            field=models.CharField(choices=[('Sandbox', 'Sandbox'), ('RTS', 'RTS'), ('FPS', 'FPS'), ('MOBA', 'MOBA'), ('RPG', 'RPG'), ('Simulation and sports', 'Simulation and sports'), ('Puzzlers and party games', 'Puzzlers and party games'), ('Action adventure', 'Action adventure'), ('IRL', 'IRL'), ('Other', 'Other')], default='a', max_length=50),
        ),
    ]
