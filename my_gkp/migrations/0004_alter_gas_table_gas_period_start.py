# Generated by Django 3.2.8 on 2022-04-18 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_gkp', '0003_auto_20220418_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gas_table',
            name='gas_period_start',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
