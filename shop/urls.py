from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', Shop , name='shop'),
    path('goods/<int:pk>', detail_view.as_view(), name='detail_view'),
    path('create/', form_create_goods, name='create_goods'),
    path('contacts/', contacts, name='contacts'),
]
