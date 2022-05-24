# Generated by Django 4.0.4 on 2022-05-24 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_journal_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='type',
            field=models.CharField(choices=[('Bullet', 'Bullet'), ('Food', 'Food'), ('Travel', 'Travel'), ('Sport', 'Sport')], max_length=6),
        ),
    ]
