# Generated by Django 4.1.2 on 2022-10-14 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='status',
            field=models.IntegerField(choices=[(1, 'Si'), (2, 'No')], default=1),
            preserve_default=False,
        ),
    ]
