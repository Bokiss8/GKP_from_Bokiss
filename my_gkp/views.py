from email import message
from itertools import count
import json
import datetime
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from .models import Gas_table, User, Res_1_zona_table, Res_2_zona_table, Res_3_zona_table, Water_table, Gas_import_table, Rent_table, Trash_table, Internet_table


def index(request):
    return render(request, "my_gkp/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "my_gkp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "my_gkp/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "my_gkp/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "my_gkp/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "my_gkp/register.html")
#--------------------------------------------------------------------------------------------------
def indicator_gas(request):
    print("indicator_gas work")
    count_table = Gas_table.objects.filter(gas_user=request.user).order_by('-id').count()
    print(f"count_table={count_table}")

    if request.method == "POST":
        print(f"request_indicator={request.POST}")
        indicator_last = request.POST["indicator_last"]
        indicator_new = request.POST["indicator_new"]
        tarif = request.POST["tarif"]
        userid = request.POST["userid"]
        period_start = request.POST["date_start"]
        period_end = request.POST["date_end"]
        print(f"indicator_last={indicator_last}")
        print(f"indicator_new={indicator_new}")
        print(f"tarif={tarif}")
        print(f"user_id={userid}")
        user_name = User.objects.get(id=userid)
        print(f"user_name={user_name}")
        indicator_date = datetime.datetime.now()
        print(f"date={indicator_date}")
        mydate = indicator_date.strftime("%d.%m.%Y")
        print(f"datemy={mydate}")
        print(f"period_start={period_start}")
        print(f"period_end={period_end}")
        minus = int(indicator_new) - int(indicator_last)
        suma = round(minus*float(tarif), 2)
        print(f"minus={minus}")
        print(f"suma={suma}")
     
        gas = Gas_table.objects.create(gas_user=user_name, gas_date=mydate, gas_period_start=period_start, gas_period_end=period_end, gas_last=indicator_last, gas_new=indicator_new, gas_rezult=minus, gas_tarif=tarif, gas_suma=suma)
        gas.save()
          #  current_lot = Lot.objects.get(pk=lot.id)
           # print(f"lotid={current_lot}")
        return HttpResponseRedirect(reverse("list_gas"))  
       # return render(request, 'my_gkp/indicator_gas.html', {
              
               # 'message_ok': "дані успішно збережені!"
              
               # })
    elif count_table > 0:
        print(f"request_indicator={request.GET}")
        print(f"request_indicator={request.user}")
        print(f"request_indicator={request.user.id}")
        last_element = Gas_table.objects.filter(gas_user=request.user).order_by('-id').first()
        last_indicator = last_element.gas_new
        last_tarif = last_element.gas_tarif
        print(last_indicator)
        return render(request, "my_gkp/indicator_gas.html", {
             
                #'message_err': "щось пішло не так!"
                "last_indicator": last_indicator,
                "last_tarif": last_tarif
                })
    else:
        #
        return render(request, "my_gkp/indicator_gas.html", {
             
                #'message_err': "щось пішло не так!"
                #"last_indicator": last_indicator,
                #"last_tarif": last_tarif
                })
#--------------------------------------------------------------------------------------------------
def indicator_res_1(request):
    print("indicator_res_1 work")
    count_table = Res_1_zona_table.objects.filter(res_user=request.user).order_by('-id').count()
    print(f"count_table={count_table}")

    if request.method == "POST":
        print(f"request_indicator={request.POST}")
        indicator_last = request.POST["indicator_last"]
        indicator_new = request.POST["indicator_new"]
        tarif = request.POST["tarif"]
        userid = request.POST["userid"]
        period_start = request.POST["date_start"]
        period_end = request.POST["date_end"]
        print(f"indicator_last={indicator_last}")
        print(f"indicator_new={indicator_new}")
        print(f"tarif={tarif}")
        print(f"user_id={userid}")
        user_name = User.objects.get(id=userid)
        print(f"user_name={user_name}")
        indicator_date = datetime.datetime.now()
        print(f"date={indicator_date}")
        mydate = indicator_date.strftime("%d.%m.%Y")
        print(f"datemy={mydate}")
        print(f"period_start={period_start}")
        print(f"period_end={period_end}")
        minus = int(indicator_new) - int(indicator_last)
        suma = round(minus*float(tarif), 2)
        print(f"minus={minus}")
        print(f"suma={suma}")
     
        res = Res_1_zona_table.objects.create(res_user=user_name, res_date=mydate, res_period_start=period_start, res_period_end=period_end, res_last=indicator_last, res_new=indicator_new, res_rezult=minus, res_tarif=tarif, res_suma=suma)
        res.save()
          #  current_lot = Lot.objects.get(pk=lot.id)
           # print(f"lotid={current_lot}")
        return HttpResponseRedirect(reverse("list_res_1"))  
       # return render(request, 'my_gkp/indicator_gas.html', {
              
               # 'message_ok': "дані успішно збережені!"
              
               # })
    elif count_table > 0:
        print(f"request_indicator={request.GET}")
        print(f"request_indicator={request.user}")
        print(f"request_indicator={request.user.id}")
        last_element = Res_1_zona_table.objects.filter(res_user=request.user).order_by('-id').first()
        last_indicator = last_element.res_new
        last_tarif = last_element.res_tarif
        print(last_indicator)
        return render(request, "my_gkp/indicator_res_1.html", {
             
                #'message_err': "щось пішло не так!"
                "last_indicator": last_indicator,
                "last_tarif": last_tarif
                })
    else:
        #
        return render(request, "my_gkp/indicator_res_1.html", {
             
                #'message_err': "щось пішло не так!"
                #"last_indicator": last_indicator,
                #"last_tarif": last_tarif
                })
#--------------------------------------------------------------------------------------------------
def indicator_res_2(request):
    print("indicator_res_2 work")
    count_table = Res_2_zona_table.objects.filter(res_user=request.user).order_by('-id').count()
    print(f"count_table={count_table}")

    if request.method == "POST":
        print(f"request_indicator={request.POST}")
        indicator_last = request.POST["indicator_last"]
        indicator_new = request.POST["indicator_new"]
        indicator_last_2 = request.POST["indicator_last_2"]
        indicator_new_2 = request.POST["indicator_new_2"]
        tarif = request.POST["tarif"]
        userid = request.POST["userid"]
        period_start = request.POST["date_start"]
        period_end = request.POST["date_end"]
        print(f"indicator_last={indicator_last}")
        print(f"indicator_new={indicator_new}")
        print(f"indicator_last_2={indicator_last_2}")
        print(f"indicator_new_2={indicator_new_2}")
        print(f"tarif={tarif}")
        print(f"user_id={userid}")
        user_name = User.objects.get(id=userid)
        print(f"user_name={user_name}")
        indicator_date = datetime.datetime.now()
        print(f"date={indicator_date}")
        mydate = indicator_date.strftime("%d.%m.%Y")
        print(f"datemy={mydate}")
        print(f"period_start={period_start}")
        print(f"period_end={period_end}")
        minus = int(indicator_new) - int(indicator_last)
        minus_2 = int(indicator_new_2) - int(indicator_last_2)
        suma_1 = round(minus*float(tarif)*1, 2)
        tarif_2 = float(tarif)*0.5
        suma_2 = round(minus_2*tarif_2, 2)
        suma = suma_1+suma_2
        print(f"tarif_2={tarif_2}")
        print(f"minus={minus}")
        print(f"minus_2={minus_2}")
        print(f"suma_1={suma_1}")
        print(f"suma_2={suma_2}")
        print(f"suma={suma}")
     
        res = Res_2_zona_table.objects.create(res_user=user_name, res_date=mydate, res_period_start=period_start, res_period_end=period_end, res_last=indicator_last, res_new=indicator_new, res_last_2=indicator_last_2, res_new_2=indicator_new_2, res_rezult=minus, res_rezult_2=minus_2, res_tarif=tarif, res_tarif_2=tarif_2, res_suma_1=suma_1, res_suma_2=suma_2, res_suma=suma)
        res.save()
        return HttpResponseRedirect(reverse("list_res_2"))  

    elif count_table > 0:
        print(f"request_indicator={request.GET}")
        print(f"request_indicator={request.user}")
        print(f"request_indicator={request.user.id}")
        last_element = Res_2_zona_table.objects.filter(res_user=request.user).order_by('-id').first()
        last_indicator = last_element.res_new
        last_indicator_2 =last_element.res_new_2
        last_tarif = last_element.res_tarif
        print(last_indicator)
        return render(request, "my_gkp/indicator_res_2.html", {
                "last_indicator": last_indicator,
                "last_indicator_2": last_indicator_2,
                "last_tarif": last_tarif
                })
    else:
        #
        return render(request, "my_gkp/indicator_res_2.html", {
             
                #'message_err': "щось пішло не так!"
                #"last_indicator": last_indicator,
                #"last_tarif": last_tarif
                })
#--------------------------------------------------------------------------------------------------
def indicator_res_3(request):
    print("indicator_res_3 work")
    count_table = Res_3_zona_table.objects.filter(res_user=request.user).order_by('-id').count()
    print(f"count_table={count_table}")

    if request.method == "POST":
        print(f"request_indicator={request.POST}")
        indicator_last = request.POST["indicator_last"]
        indicator_new = request.POST["indicator_new"]
        indicator_last_2 = request.POST["indicator_last_2"]
        indicator_new_2 = request.POST["indicator_new_2"]
        indicator_last_3 = request.POST["indicator_last_3"]
        indicator_new_3 = request.POST["indicator_new_3"]
        tarif_2 = request.POST["tarif"]
        userid = request.POST["userid"]
        period_start = request.POST["date_start"]
        period_end = request.POST["date_end"]
        print(f"indicator_last={indicator_last}")
        print(f"indicator_new={indicator_new}")
        print(f"indicator_last_2={indicator_last_2}")
        print(f"indicator_new_2={indicator_new_2}")
        print(f"indicator_last_3={indicator_last_3}")
        print(f"indicator_new_3={indicator_new_3}")
        print(f"user_id={userid}")
        user_name = User.objects.get(id=userid)
        print(f"user_name={user_name}")
        indicator_date = datetime.datetime.now()
        print(f"date={indicator_date}")
        mydate = indicator_date.strftime("%d.%m.%Y")
        print(f"datemy={mydate}")
        print(f"period_start={period_start}")
        print(f"period_end={period_end}")
        minus = int(indicator_new) - int(indicator_last)
        minus_2 = int(indicator_new_2) - int(indicator_last_2)
        minus_3 = int(indicator_new_3) - int(indicator_last_3)
        tarif = float(tarif_2)*1.5
        tarif_3 = float(tarif_2)*0.4
        suma_1 = round(minus*tarif, 2)
        suma_2 = round(minus_2*float(tarif_2), 2)
        suma_3 = round(minus_3*tarif_3, 2)
        suma = suma_1+suma_2+suma_3
        print(f"tarif={tarif}")
        print(f"tarif_2={tarif_2}")
        print(f"tarif_3={tarif_3}")
        print(f"minus={minus}")
        print(f"minus_2={minus_2}")
        print(f"minus_3={minus_3}")
        print(f"suma_1={suma_1}")
        print(f"suma_2={suma_2}")
        print(f"suma_3={suma_3}")
        print(f"suma={suma}")
     
        res = Res_3_zona_table.objects.create(res_user=user_name, res_date=mydate, res_period_start=period_start, res_period_end=period_end, res_last=indicator_last, res_new=indicator_new, res_last_2=indicator_last_2, res_new_2=indicator_new_2, res_last_3=indicator_last_3, res_new_3=indicator_new_3, res_rezult=minus, res_rezult_2=minus_2, res_rezult_3=minus_3, res_tarif=tarif, res_tarif_2=tarif_2, res_tarif_3=tarif_3, res_suma_1=suma_1, res_suma_2=suma_2, res_suma_3=suma_3, res_suma=suma)
        res.save()
        return HttpResponseRedirect(reverse("list_res_3"))  

    elif count_table > 0:
        print(f"request_indicator={request.GET}")
        print(f"request_indicator={request.user}")
        print(f"request_indicator={request.user.id}")
        last_element = Res_3_zona_table.objects.filter(res_user=request.user).order_by('-id').first()
        last_indicator = last_element.res_new
        last_indicator_2 = last_element.res_new_2
        last_indicator_3 = last_element.res_new_3
        last_tarif = last_element.res_tarif_2
        print(last_indicator)
        return render(request, "my_gkp/indicator_res_3.html", {
                "last_indicator": last_indicator,
                "last_indicator_2": last_indicator_2,
                "last_indicator_3": last_indicator_3,
                "last_tarif": last_tarif
                })
    else:
        #
        return render(request, "my_gkp/indicator_res_3.html", {
             
                #'message_err': "щось пішло не так!"
                #"last_indicator": last_indicator,
                #"last_tarif": last_tarif
                })
#--------------------------------------------------------------------------------------------------
def indicator_water(request):
    print("indicator_water work")
    count_table = Water_table.objects.filter(water_user=request.user).order_by('-id').count()
    print(f"count_table={count_table}")

    if request.method == "POST":
        print(f"request_indicator={request.POST}")
        indicator_last = request.POST["indicator_last"]
        indicator_new = request.POST["indicator_new"]
        tarif = request.POST["tarif"]
        abonplata = request.POST["abonplata"]
        if abonplata == '':
            abonplata = 0
        userid = request.POST["userid"]
        period_start = request.POST["date_start"]
        period_end = request.POST["date_end"]
        print(f"indicator_last={indicator_last}")
        print(f"indicator_new={indicator_new}")
        print(f"tarif={tarif}")
        print(f"user_id={userid}")
        user_name = User.objects.get(id=userid)
        print(f"user_name={user_name}")
        indicator_date = datetime.datetime.now()
        print(f"date={indicator_date}")
        mydate = indicator_date.strftime("%d.%m.%Y")
        print(f"datemy={mydate}")
        print(f"period_start={period_start}")
        print(f"period_end={period_end}")
        minus = int(indicator_new) - int(indicator_last)
        suma = round(minus*float(tarif) + float(abonplata), 2)
        print(f"minus={minus}")
        print(f"abonplata={abonplata}")
        print(f"suma={suma}")
     
        water = Water_table.objects.create(water_user=user_name, water_date=mydate, water_period_start=period_start, water_period_end=period_end, water_last=indicator_last, water_new=indicator_new, water_rezult=minus, water_tarif=tarif, water_abonplata=abonplata, water_suma=suma)
        water.save()
          #  current_lot = Lot.objects.get(pk=lot.id)
           # print(f"lotid={current_lot}")
        return HttpResponseRedirect(reverse("list_water"))  
       
    elif count_table > 0:
        print(f"request_indicator={request.GET}")
        print(f"request_indicator={request.user}")
        print(f"request_indicator={request.user.id}")
        last_element = Water_table.objects.filter(water_user=request.user).order_by('-id').first()
        last_indicator = last_element.water_new
        last_tarif = last_element.water_tarif
        last_abonplata = last_element.water_abonplata
        print(last_indicator)
        return render(request, "my_gkp/indicator_water.html", {
             
                #'message_err': "щось пішло не так!"
                "last_indicator": last_indicator,
                "last_tarif": last_tarif,
                "last_abonplata": last_abonplata
                })
    else:
        #
        return render(request, "my_gkp/indicator_water.html", {
             
                #'message_err': "щось пішло не так!"
                #"last_indicator": last_indicator,
                #"last_tarif": last_tarif
                })
#--------------------------------------------------------------------------------------------------
def list_gas(request):
    print("list_gas work")
    gaslist = Gas_table.objects.all()
    dlina = Gas_table.objects.all().count()
    fir = Gas_table.objects.all().order_by('-id').first()
    lastindik = fir.gas_new
    print(gaslist)
    print(dlina)
    print(fir)
    print(lastindik)
    return render(request, "my_gkp/list_gas.html", {
             
                #'message_err': "щось пішло не так!"
                "listgas": Gas_table.objects.filter(gas_user=request.user).order_by('-id')
                })
#--------------------------------------------------------------------------------------------------
def list_res_1(request):
    print("list_res_1 work")
  
    return render(request, "my_gkp/list_res_1.html", {
             
                #'message_err': "щось пішло не так!"
                "listres": Res_1_zona_table.objects.filter(res_user=request.user).order_by('-id')
                })
#--------------------------------------------------------------------------------------------------
def list_res_2(request):
    print("list_res_2 work")
   
    return render(request, "my_gkp/list_res_2.html", {
             
                #'message_err': "щось пішло не так!"
                "listres": Res_2_zona_table.objects.filter(res_user=request.user).order_by('-id')
                })
#--------------------------------------------------------------------------------------------------
def list_res_3(request):
    print("list_res_3 work")
   
    return render(request, "my_gkp/list_res_3.html", {
             
                #'message_err': "щось пішло не так!"
                "listres": Res_3_zona_table.objects.filter(res_user=request.user).order_by('-id')
                })
#--------------------------------------------------------------------------------------------------
def list_water(request):
    print("list_water work")
   
    return render(request, "my_gkp/list_water.html", {
             
                #'message_err': "щось пішло не так!"
                "listwater": Water_table.objects.filter(water_user=request.user).order_by('-id')
                })
#--------------------------------------------------------------------------------------------------
def import_gas(request):
    print("import_gas work")
    count_table = Gas_table.objects.filter(gas_user=request.user).order_by('-id').count()
    print(f"count_table={count_table}")

    if request.method == "POST":
        print(f"request_indicator={request.POST}")
        import_gas_kyb = request.POST["import_kyb"]
        tarif = request.POST["tarif"]
        userid = request.POST["userid"]
        period_start = request.POST["date_start"]
        period_end = request.POST["date_end"]
        print(f"import_gas_kyb={import_gas_kyb}")
        print(f"tarif={tarif}")
        print(f"user_id={userid}")
        user_name = User.objects.get(id=userid)
        print(f"user_name={user_name}")
        indicator_date = datetime.datetime.now()
        print(f"date={indicator_date}")
        mydate = indicator_date.strftime("%d.%m.%Y")
        print(f"datemy={mydate}")
        print(f"period_start={period_start}")
        print(f"period_end={period_end}")
        sum_import = round(int(import_gas_kyb) * float(tarif) / 12, 2)
        print(f"sum_import={sum_import}")
        
        gas_import = Gas_import_table.objects.create(gas_import_user=user_name, gas_import_date=mydate, gas_import_period_start=period_start, gas_import_period_end=period_end, gas_import_rezult=import_gas_kyb, gas_import_tarif=tarif, gas_import_suma=sum_import)
        gas_import.save()
          #  current_lot = Lot.objects.get(pk=lot.id)
           # print(f"lotid={current_lot}")
        return HttpResponseRedirect(reverse("import_gas"))  
       # return render(request, 'my_gkp/indicator_gas.html', {
              
               # 'message_ok': "дані успішно збережені!"
              
               # })
    elif count_table > 0:
        print(f"request_indicator={request.GET}")
        print(f"request_indicator={request.user}")
        print(f"request_indicator={request.user.id}")
        count_table_import = Gas_import_table.objects.filter(gas_import_user=request.user).order_by('-id').count()
        last_import_rez = ''
        last_import_tarif = ''
        if count_table_import > 0:
            #
            last_element = Gas_import_table.objects.filter(gas_import_user=request.user).order_by('-id').first()
            last_import_rez = last_element.gas_import_rezult
            last_import_tarif = last_element.gas_import_tarif
            print(f"last_import={last_import_rez}")
        indicator_date = datetime.datetime.now()
        print(f"date={indicator_date}")
        mydate = indicator_date.strftime("%d.%m.%Y")
        year_today = indicator_date.strftime("%Y")
        print(f"datemy={mydate}")
        print(f"year_today={year_today}")
        year_today_min2 = int(year_today) - 2
        year_today_min1 = int(year_today) - 1
        print(f"year_today_min2={year_today_min2}")
        year_start = str(year_today_min2) + "-10-01"
        year_end = str(year_today_min1) + "-09-20"
        findik = Gas_table.objects.filter(gas_user=request.user).order_by('-id').filter(gas_period_start__gte=year_start, gas_period_start__lt=year_end)
        proverka = findik.count()
        print(f"findik={findik}")
        print(f"proverka={proverka}")
        mymessage_ok = ""
        mymessage_err = ""
        sum_all = 0
        if proverka >= 1:
            #
            for sum in findik:
                sum_all = sum_all + sum.gas_rezult
                print(f"sum_all={sum_all}")
        # тариф нижче 1,79 прописаний вручну        
        sum_year = round(sum_all * 1.79 / 12, 2)
        if proverka < 12:
            mymessage_err = "недостатньо даних для автоматичного розрахунку! лише " + str(proverka) + " місяців взято в розрахунок"
        else:
            mymessage_ok = "Ваш об'єм споживання газу на протязі минулого «газового року» становить " + str(sum_all) + " (куб)"
        print(f"sum_year={sum_year}")

        return render(request, "my_gkp/import_gas.html", {
             
                #'message_err': "щось пішло не так!"
                "last_import": last_import_rez,
                "sum_year": sum_year,
                "last_import_tarif": last_import_tarif,
                "mymessage_ok": mymessage_ok,
                "mymessage_err": mymessage_err,
                "listgasimport": Gas_import_table.objects.filter(gas_import_user=request.user).order_by('-id')
                })
    else:
        #print(f"чтото пошло не так")
        return render(request, "my_gkp/import_gas.html", {
             
                #'message_err': "щось пішло не так!"
                #"last_indicator": last_indicator,
                #"last_tarif": last_tarif
                "listgasimport": Gas_import_table.objects.filter(gas_import_user=request.user).order_by('-id')
                })
#--------------------------------------------------------------------------------------------------
def rent(request):
    print("rent work")
    count_table = Rent_table.objects.filter(rent_user=request.user).order_by('-id').count()
    print(f"count_table={count_table}")

    if request.method == "POST":
        print(f"request_indicator={request.POST}")
        rent = request.POST["rent"]
        userid = request.POST["userid"]
        period_start = request.POST["date_start"]
        period_end = request.POST["date_end"]
        print(f"user_id={userid}")
        user_name = User.objects.get(id=userid)
        print(f"user_name={user_name}")
        indicator_date = datetime.datetime.now()
        print(f"date={indicator_date}")
        mydate = indicator_date.strftime("%d.%m.%Y")
        print(f"datemy={mydate}")
        print(f"period_start={period_start}")
        print(f"period_end={period_end}")
        print(f"rent={rent}")
        #++++++++++++++++++++++++++++++++++++++++++
        rent_input = Rent_table.objects.create(rent_user=user_name, rent_date=mydate, rent_period_start=period_start, rent_period_end=period_end, rent_suma=rent)
        rent_input.save()
         
        return HttpResponseRedirect(reverse("rent"))  
       
    elif count_table > 0:
        print(f"request_indicator={request.GET}")
        print(f"request_indicator={request.user}")
        print(f"request_indicator={request.user.id}")
        last_element = Rent_table.objects.filter(rent_user=request.user).order_by('-id').first()
        last_rent = last_element.rent_suma
        print(f"last_rent={last_rent}")

        return render(request, "my_gkp/rent.html", {
             
                #'message_err': "щось пішло не так!"
                "last_rent": last_rent,
                "listrent": Rent_table.objects.filter(rent_user=request.user).order_by('-id')
                })
    else:
        #
        return render(request, "my_gkp/rent.html", {
             
                #'message_err': "щось пішло не так!"
                #"last_indicator": last_indicator,
                #"last_tarif": last_tarif
                "listrent": Rent_table.objects.filter(rent_user=request.user).order_by('-id')
                })
#--------------------------------------------------------------------------------------------------
def trash(request):
    print("trash work")
    count_table = Trash_table.objects.filter(trash_user=request.user).order_by('-id').count()
    print(f"count_table={count_table}")

    if request.method == "POST":
        print(f"request_indicator={request.POST}")
        trash = request.POST["trash"]
        userid = request.POST["userid"]
        period_start = request.POST["date_start"]
        period_end = request.POST["date_end"]
        print(f"user_id={userid}")
        user_name = User.objects.get(id=userid)
        print(f"user_name={user_name}")
        indicator_date = datetime.datetime.now()
        print(f"date={indicator_date}")
        mydate = indicator_date.strftime("%d.%m.%Y")
        print(f"datemy={mydate}")
        print(f"period_start={period_start}")
        print(f"period_end={period_end}")
        print(f"trash={trash}")
        #++++++++++++++++++++++++++++++++++++++++++
        trash_input = Trash_table.objects.create(trash_user=user_name, trash_date=mydate, trash_period_start=period_start, trash_period_end=period_end, trash_suma=trash)
        trash_input.save()
         
        return HttpResponseRedirect(reverse("trash"))  
       
    elif count_table > 0:
        print(f"request_indicator={request.GET}")
        print(f"request_indicator={request.user}")
        print(f"request_indicator={request.user.id}")
        last_element = Trash_table.objects.filter(trash_user=request.user).order_by('-id').first()
        last_trash = last_element.trash_suma
        print(f"last_trash={last_trash}")

        return render(request, "my_gkp/trash.html", {

            #    'message_err': "щось пішло не так!"
                "last_trash": last_trash,
                "listtrash": Trash_table.objects.filter(trash_user=request.user).order_by('-id')
                })
    else:
        #
        return render(request, "my_gkp/trash.html", {
             
                #'message_err': "щось пішло не так!"
                #"last_indicator": last_indicator,
                #"last_tarif": last_tarif
                "listtrash": Trash_table.objects.filter(trash_user=request.user).order_by('-id')
                })
#--------------------------------------------------------------------------------------------------
def internet(request):
    print("internet work")
    count_table = Internet_table.objects.filter(internet_user=request.user).order_by('-id').count()
    print(f"count_table={count_table}")

    if request.method == "POST":
        print(f"request_indicator={request.POST}")
        internet = request.POST["internet"]
        userid = request.POST["userid"]
        period_start = request.POST["date_start"]
        period_end = request.POST["date_end"]
        print(f"user_id={userid}")
        user_name = User.objects.get(id=userid)
        print(f"user_name={user_name}")
        indicator_date = datetime.datetime.now()
        print(f"date={indicator_date}")
        mydate = indicator_date.strftime("%d.%m.%Y")
        print(f"datemy={mydate}")
        print(f"period_start={period_start}")
        print(f"period_end={period_end}")
        print(f"internet={internet}")
        #++++++++++++++++++++++++++++++++++++++++++
        internet_input = Internet_table.objects.create(internet_user=user_name, internet_date=mydate, internet_period_start=period_start, internet_period_end=period_end, internet_suma=internet)
        internet_input.save()
         
        return HttpResponseRedirect(reverse("internet"))  
       
    elif count_table > 0:
        print(f"request_indicator={request.GET}")
        print(f"request_indicator={request.user}")
        print(f"request_indicator={request.user.id}")
        last_element = Internet_table.objects.filter(internet_user=request.user).order_by('-id').first()
        last_internet = last_element.internet_suma
        print(f"last_internet={last_internet}")

        return render(request, "my_gkp/internet.html", {
             
                #'message_err': "щось пішло не так!"
                "last_internet": last_internet,
                "listinternet": Internet_table.objects.filter(internet_user=request.user).order_by('-id')
                })
    else:
        #
        return render(request, "my_gkp/internet.html", {
             
                #'message_err': "щось пішло не так!"
                #"last_indicator": last_indicator,
                #"last_tarif": last_tarif
                "listinternet": Internet_table.objects.filter(internet_user=request.user).order_by('-id')
                })
#--------------------------------------------------------------------------------------------------