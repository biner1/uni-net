# Generated by Django 3.1.3 on 2021-09-07 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0001_initial'),
        ('users', '0002_auto_20210907_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='user_role',
        ),
        migrations.AddField(
            model_name='customuser',
            name='stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lectures.studentstage'),
        ),
    ]
