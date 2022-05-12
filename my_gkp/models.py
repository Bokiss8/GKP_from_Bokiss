from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date

# Create your models here.
#----------------------------------------------------------------------------------
class User(AbstractUser):
    pass
#----------------------------------------------------------------------------------
class Gas_table(models.Model):
    gas_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    gas_date = models.DateTimeField(auto_now=True)
    gas_period_start = models.DateField(default=date.today)
    gas_period_end = models.DateField(default=date.today)
    gas_last = models.IntegerField()
    gas_new = models.IntegerField()
    gas_rezult = models.IntegerField(default=0)
    gas_tarif = models.FloatField()
    gas_suma = models.FloatField()

    def __str__(self):
        gas_time = self.gas_date.strftime("%d.%m.%Y")
        return f"{self.id}: {self.gas_user} and {gas_time} and {self.gas_period_start} and {self.gas_period_end} and {self.gas_last} and {self.gas_new} and {self.gas_rezult} and {self.gas_tarif} and {self.gas_suma}"
#----------------------------------------------------------------------------------
class Res_1_zona_table(models.Model):
    res_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    res_date = models.DateTimeField(auto_now=True)
    res_period_start = models.DateField(default=date.today)
    res_period_end = models.DateField(default=date.today)
    res_last = models.IntegerField()
    res_new = models.IntegerField()
    res_rezult = models.IntegerField(default=0)
    res_tarif = models.FloatField()
    res_suma = models.FloatField()

    def __str__(self):
        res_time = self.res_date.strftime("%d.%m.%Y")
        return f"{self.id}: {self.res_user} and {res_time} and {self.res_period_start} and {self.res_period_end} and {self.res_last} and {self.res_new} and {self.res_rezult} and {self.res_tarif} and {self.res_suma}"
#----------------------------------------------------------------------------------
class Res_2_zona_table(models.Model):
    res_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    res_date = models.DateTimeField(auto_now=True)
    res_period_start = models.DateField(default=date.today)
    res_period_end = models.DateField(default=date.today)
    res_last = models.IntegerField()
    res_new = models.IntegerField()
    res_last_2 = models.IntegerField()
    res_new_2 = models.IntegerField()
    res_rezult = models.IntegerField(default=0)
    res_rezult_2 = models.IntegerField(default=0)
    res_tarif = models.FloatField()
    res_tarif_2 = models.FloatField()
    res_suma_1 = models.FloatField()
    res_suma_2 = models.FloatField()
    res_suma = models.FloatField()

    def __str__(self):
        res_time = self.res_date.strftime("%d.%m.%Y")
        return f"{self.id}: {self.res_user} and {res_time} and {self.res_period_start} and {self.res_period_end} and {self.res_last} and {self.res_new} and{self.res_last_2} and {self.res_new_2} and {self.res_rezult} and {self.res_rezult_2} and {self.res_tarif} and {self.res_tarif_2} and {self.res_suma_1} and {self.res_suma_2} and {self.res_suma}"
#----------------------------------------------------------------------------------
class Res_3_zona_table(models.Model):
    res_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    res_date = models.DateTimeField(auto_now=True)
    res_period_start = models.DateField(default=date.today)
    res_period_end = models.DateField(default=date.today)
    res_last = models.IntegerField()
    res_new = models.IntegerField()
    res_last_2 = models.IntegerField()
    res_new_2 = models.IntegerField()
    res_last_3 = models.IntegerField()
    res_new_3 = models.IntegerField()
    res_rezult = models.IntegerField(default=0)
    res_rezult_2 = models.IntegerField(default=0)
    res_rezult_3 = models.IntegerField(default=0)
    res_tarif = models.FloatField()
    res_tarif_2 = models.FloatField()
    res_tarif_3 = models.FloatField()
    res_suma_1 = models.FloatField()
    res_suma_2 = models.FloatField()
    res_suma_3 = models.FloatField()
    res_suma = models.FloatField()

    def __str__(self):
        res_time = self.res_date.strftime("%d.%m.%Y")
        return f"{self.id}: {self.res_user} and {res_time} and {self.res_period_start} and {self.res_period_end} and {self.res_last} and {self.res_new} and {self.res_last_2} and {self.res_new_2} and {self.res_last_3} and {self.res_new_3} and {self.res_rezult} and {self.res_rezult_2} and {self.res_rezult_3} and {self.res_tarif} and {self.res_tarif_2} and {self.res_tarif_3} and {self.res_suma_1} and {self.res_suma_2} and {self.res_suma_3} and {self.res_suma}"
#----------------------------------------------------------------------------------
class Water_table(models.Model):
    water_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    water_date = models.DateTimeField(auto_now=True)
    water_period_start = models.DateField(default=date.today)
    water_period_end = models.DateField(default=date.today)
    water_last = models.IntegerField()
    water_new = models.IntegerField()
    water_rezult = models.IntegerField(default=0)
    water_tarif = models.FloatField()
    water_abonplata = models.FloatField()
    water_suma = models.FloatField()

    def __str__(self):
        water_time = self.water_date.strftime("%d.%m.%Y")
        return f"{self.id}: {self.water_user} and {water_time} and {self.water_period_start} and {self.water_period_end} and {self.water_last} and {self.water_new} and {self.water_rezult} and {self.water_tarif} and {self.water_abonplata} and {self.water_suma}"
#----------------------------------------------------------------------------------
class Gas_import_table(models.Model):
    gas_import_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    gas_import_date = models.DateTimeField(auto_now=True)
    gas_import_period_start = models.DateField(default=date.today)
    gas_import_period_end = models.DateField(default=date.today)
    gas_import_rezult = models.IntegerField(default=0)
    gas_import_tarif = models.FloatField()
    gas_import_suma = models.FloatField()

    def __str__(self):
        gas_import_time = self.gas_import_date.strftime("%d.%m.%Y")
        return f"{self.id}: {self.gas_import_user} and {gas_import_time} and {self.gas_import_period_start} and {self.gas_import_period_end} and {self.gas_import_rezult} and {self.gas_import_tarif} and {self.gas_import_suma}"
#----------------------------------------------------------------------------------
class Rent_table(models.Model):
    rent_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    rent_date = models.DateTimeField(auto_now=True)
    rent_period_start = models.DateField(default=date.today)
    rent_period_end = models.DateField(default=date.today)
    rent_suma = models.FloatField()

    def __str__(self):
        rent_time = self.rent_date.strftime("%d.%m.%Y")
        return f"{self.id}: {self.rent_user} and {rent_time} and {self.rent_period_start} and {self.rent_period_end} and {self.rent_suma}"
#----------------------------------------------------------------------------------
class Trash_table(models.Model):
    trash_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    trash_date = models.DateTimeField(auto_now=True)
    trash_period_start = models.DateField(default=date.today)
    trash_period_end = models.DateField(default=date.today)
    trash_suma = models.FloatField()

    def __str__(self):
        trash_time = self.trash_date.strftime("%d.%m.%Y")
        return f"{self.id}: {self.trash_user} and {trash_time} and {self.trash_period_start} and {self.trash_period_end} and {self.trash_suma}"
#----------------------------------------------------------------------------------
class Internet_table(models.Model):
    internet_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    internet_date = models.DateTimeField(auto_now=True)
    internet_period_start = models.DateField(default=date.today)
    internet_period_end = models.DateField(default=date.today)
    internet_suma = models.FloatField()

    def __str__(self):
        internet_time = self.internet_date.strftime("%d.%m.%Y")
        return f"{self.id}: {self.internet_user} and {internet_time} and {self.internet_period_start} and {self.internet_period_end} and {self.internet_suma}"
#----------------------------------------------------------------------------------