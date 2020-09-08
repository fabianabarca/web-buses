# Generated by Django 3.0.8 on 2020-08-20 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_id', models.IntegerField()),
                ('agency_id', models.CharField(max_length=16)),
                ('route_short_name', models.CharField(max_length=16)),
                ('route_long_name', models.CharField(max_length=32)),
            ],
        ),
    ]