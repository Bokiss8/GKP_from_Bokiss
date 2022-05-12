# Generated by Django 3.2.9 on 2022-05-05 07:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_gkp', '0012_rent_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trash_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trash_date', models.DateTimeField(auto_now=True)),
                ('trash_period_start', models.DateField(default=datetime.date.today)),
                ('trash_period_end', models.DateField(default=datetime.date.today)),
                ('trash_suma', models.FloatField()),
                ('trash_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Internet_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internet_date', models.DateTimeField(auto_now=True)),
                ('internet_period_start', models.DateField(default=datetime.date.today)),
                ('internet_period_end', models.DateField(default=datetime.date.today)),
                ('internet_suma', models.FloatField()),
                ('internet_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
