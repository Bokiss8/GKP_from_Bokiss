from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("indicator_gas", views.indicator_gas, name="indicator_gas"),
    path("indicator_res_1", views.indicator_res_1, name="indicator_res_1"),
    path("indicator_res_2", views.indicator_res_2, name="indicator_res_2"),
    path("indicator_res_3", views.indicator_res_3, name="indicator_res_3"),
    path("indicator_water", views.indicator_water, name="indicator_water"),
    path("list_gas", views.list_gas, name="list_gas"),
    path("list_res_1", views.list_res_1, name="list_res_1"),
    path("list_res_2", views.list_res_2, name="list_res_2"),
    path("list_res_3", views.list_res_3, name="list_res_3"),
    path("list_water", views.list_water, name="list_water"),
    path("import_gas", views.import_gas, name="import_gas"),
    path("rent", views.rent, name="rent"),
    path("trash", views.trash, name="trash"),
    path("internet", views.internet, name="internet"),

    # API Routes
   # path("posts", views.composepost, name="composepost"),
    #path("posts/<str:posts>", views.listposts, name="listposts"),
    #path("statuslike", views.statuslike, name="statuslike"),
    #path("edit", views.edit, name="edit"),
    #path("comment", views.comment, name="comment"),
    #path("subscribeunsubscribe", views.subscribeunsubscribe, name="subscribeunsubscribe")
]
