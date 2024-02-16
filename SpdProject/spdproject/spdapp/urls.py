from django.urls import path

from . import views

urlpatterns = [
    path("",views.indexfunction,name="index"),
    path("registration", views.registration, name="registration"),
    path("userlogin",views.userlogin,name="userlogin"),
    path("checkuserlogin",views.checkuserlogin,name="checkuserlogin"),

    path("userhome",views.userhome,name="userhome"),
    path("userlogout",views.userlogout,name="userlogout"),
    path("Zodiacsign",views.newproject,name="zodiacsign"),
    path("spareparts",views.sparepart,name="spareparts"),
    path("checksign", views.checksign, name="checksign"),
]