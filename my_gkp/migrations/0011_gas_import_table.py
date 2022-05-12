# Generated by Django 3.2.9 on 2022-05-04 07:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_gkp', '0010_water_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gas_import_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gas_import_date', models.DateTimeField(auto_now=True)),
                ('gas_import_period_start', models.DateField(default=datetime.date.today)),
                ('gas_import_period_end', models.DateField(default=datetime.date.today)),
                ('gas_import_rezult', models.IntegerField(default=0)),
                ('gas_import_tarif', models.FloatField()),
                ('gas_import_suma', models.FloatField()),
                ('gas_import_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
