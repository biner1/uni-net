# Generated by Django 3.1.3 on 2021-09-21 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_lecturevote_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturevote',
            name='lecture',
        ),
        migrations.RemoveField(
            model_name='lecturevote',
            name='value',
        ),
    ]
