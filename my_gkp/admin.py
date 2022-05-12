from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Gas_table, Res_1_zona_table, Res_2_zona_table, Res_3_zona_table, Water_table, Gas_import_table, Rent_table, Trash_table, Internet_table

# Register your models here.|

class Gas_tableAdmin(admin.ModelAdmin):
    list_display = ("id", "gas_user", "gas_date", "gas_period_start", "gas_period_end", "gas_last", "gas_new", "gas_rezult", "gas_tarif", "gas_suma")
class Res_1_zona_tableAdmin(admin.ModelAdmin):
    list_display = ("id", "res_user", "res_date", "res_period_start", "res_period_end", "res_last", "res_new", "res_rezult", "res_tarif", "res_suma")
class Res_2_zona_tableAdmin(admin.ModelAdmin):
    list_display = ("id", "res_user", "res_date", "res_period_start", "res_period_end", "res_last", "res_new", "res_last_2", "res_new_2", "res_rezult", "res_rezult_2", "res_tarif", "res_tarif_2", "res_suma_1", "res_suma_2", "res_suma")
class Res_3_zona_tableAdmin(admin.ModelAdmin):
    list_display = ("id", "res_user", "res_date", "res_period_start", "res_period_end", "res_last", "res_new", "res_last_2", "res_new_2", "res_last_3", "res_new_3", "res_rezult", "res_rezult_2", "res_rezult_3", "res_tarif", "res_tarif_2", "res_tarif_3", "res_suma_1", "res_suma_2", "res_suma_3", "res_suma")
class Water_tableAdmin(admin.ModelAdmin):
    list_display = ("id", "water_user", "water_date", "water_period_start", "water_period_end", "water_last", "water_new", "water_rezult", "water_tarif", "water_abonplata", "water_suma")
class Gas_import_tableAdmin(admin.ModelAdmin):
    list_display = ("id", "gas_import_user", "gas_import_date", "gas_import_period_start", "gas_import_period_end", "gas_import_rezult", "gas_import_tarif", "gas_import_suma")
class Rent_tableAdmin(admin.ModelAdmin):
    list_display = ("id", "rent_user", "rent_date", "rent_period_start", "rent_period_end", "rent_suma")
class Trash_tableAdmin(admin.ModelAdmin):
    list_display = ("id", "trash_user", "trash_date", "trash_period_start", "trash_period_end", "trash_suma")
class Internet_tableAdmin(admin.ModelAdmin):
    list_display = ("id", "internet_user", "internet_date", "internet_period_start", "internet_period_end", "internet_suma")

admin.site.register(User, UserAdmin)
admin.site.register(Gas_table, Gas_tableAdmin)
admin.site.register(Res_1_zona_table, Res_1_zona_tableAdmin)
admin.site.register(Res_2_zona_table, Res_2_zona_tableAdmin)
admin.site.register(Res_3_zona_table, Res_3_zona_tableAdmin)
admin.site.register(Water_table, Water_tableAdmin)
admin.site.register(Gas_import_table, Gas_import_tableAdmin)
admin.site.register(Rent_table, Rent_tableAdmin)
admin.site.register(Trash_table, Trash_tableAdmin)
admin.site.register(Internet_table, Internet_tableAdmin)
#admin.site.register(Comment)
