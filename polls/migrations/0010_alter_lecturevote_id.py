# Generated by Django 3.2.7 on 2021-10-31 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20211018_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturevote',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]