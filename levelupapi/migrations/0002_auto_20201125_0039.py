# Generated by Django 3.1.3 on 2020-11-25 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='game_type',
            new_name='gametype',
        ),
    ]
