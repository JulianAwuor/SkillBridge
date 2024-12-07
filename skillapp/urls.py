
from django.contrib import admin
from django.urls import path
from skillapp import views

urlpatterns = [

    path('', views.index, name='index'),
    path('author/', views.author, name='author'),
    path('explore/', views.explore, name='explore'),
    path('create/', views.create, name='create'),
    path('aisha/', views.aisha, name='aisha'),
    path('grace/', views.grace, name='grace'),
    path('brian/', views.brian, name='brian'),
    path('ama/', views.ama, name='ama'),
    path('example', views.example, name='example'),
    path('aishaaccount/', views.aishaaccount, name='aishaaccount'),



#Mpesa API Urls
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),


]
