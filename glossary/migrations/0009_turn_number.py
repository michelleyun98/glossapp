# Generated by Django 4.2.7 on 2023-11-23 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glossary', '0008_turn'),
    ]

    operations = [
        migrations.AddField(
            model_name='turn',
            name='number',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
