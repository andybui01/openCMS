# Generated by Django 3.0.3 on 2020-02-26 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0003_lift_changes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lift',
            name='changes',
        ),
        migrations.AddField(
            model_name='athlete',
            name='next_attempt',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='athlete',
            name='next_weight',
            field=models.IntegerField(default=999),
        ),
        migrations.AddField(
            model_name='lift',
            name='change',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='lift',
            name='weight',
            field=models.IntegerField(default=999),
        ),
    ]
