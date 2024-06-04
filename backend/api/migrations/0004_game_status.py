# Generated by Django 5.0.4 on 2024-05-20 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_player_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.TextField(choices=[('IN_PROGRESS', 'Game in progress'), ('COMPLETED', 'Game was completed')], default='IN_PROGRESS'),
        ),
    ]
