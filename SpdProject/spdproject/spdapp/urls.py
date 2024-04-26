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
    path("checksign", views.checksign, name="checksign"),
    path('create-reg', views.create_registration, name='create_registration'),
    path('reg-list', views.registration_list, name='registration_list'),
    path('update/<int:pk>/', views.update_registration, name='update_registration'),
    path('delete/<int:pk>/', views.delete_registration, name='delete_registration'),

   ]