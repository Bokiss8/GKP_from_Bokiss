# Generated by Django 3.2.9 on 2022-05-05 06:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_gkp', '0011_gas_import_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rent_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_date', models.DateTimeField(auto_now=True)),
                ('rent_period_start', models.DateField(default=datetime.date.today)),
                ('rent_period_end', models.DateField(default=datetime.date.today)),
                ('rent_suma', models.FloatField()),
                ('rent_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
