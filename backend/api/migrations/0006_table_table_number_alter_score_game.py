# Generated by Django 5.0.4 on 2024-06-24 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_rename_scorer_type_game_scorer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='table_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='score',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scores', to='api.game'),
        ),
    ]
