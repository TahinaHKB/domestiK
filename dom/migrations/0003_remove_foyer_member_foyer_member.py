# Generated by Django 5.0.4 on 2024-05-29 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dom', '0002_foyer_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foyer',
            name='member',
        ),
        migrations.AddField(
            model_name='foyer',
            name='member',
            field=models.ManyToManyField(to='dom.membre'),
        ),
    ]
