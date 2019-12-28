# Generated by Django 3.0 on 2019-12-28 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempt', models.IntegerField(default=1)),
                ('weight', models.IntegerField(default=0)),
                ('result', models.NullBooleanField(default=None)),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='session.Athlete')),
            ],
        ),
    ]
