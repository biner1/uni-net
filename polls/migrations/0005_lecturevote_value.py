# Generated by Django 3.1.3 on 2021-09-21 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_lecturevote_lecture'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturevote',
            name='value',
            field=models.CharField(choices=[('upvote', 'upvote'), ('downvote', 'downvote')], max_length=20, null=True),
        ),
    ]
