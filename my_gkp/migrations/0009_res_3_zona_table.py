# Generated by Django 3.2.9 on 2022-04-29 12:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_gkp', '0008_res_2_zona_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Res_3_zona_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res_date', models.DateTimeField(auto_now=True)),
                ('res_period_start', models.DateField(default=datetime.date.today)),
                ('res_period_end', models.DateField(default=datetime.date.today)),
                ('res_last', models.IntegerField()),
                ('res_new', models.IntegerField()),
                ('res_last_2', models.IntegerField()),
                ('res_new_2', models.IntegerField()),
                ('res_last_3', models.IntegerField()),
                ('res_new_3', models.IntegerField()),
                ('res_rezult', models.IntegerField(default=0)),
                ('res_rezult_2', models.IntegerField(default=0)),
                ('res_rezult_3', models.IntegerField(default=0)),
                ('res_tarif', models.FloatField()),
                ('res_tarif_2', models.FloatField()),
                ('res_tarif_3', models.FloatField()),
                ('res_suma_1', models.FloatField()),
                ('res_suma_2', models.FloatField()),
                ('res_suma_3', models.FloatField()),
                ('res_suma', models.FloatField()),
                ('res_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
