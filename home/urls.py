from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    
  path("", views.index, name='index')  ,
  path("about", views.about, name='about') , 
  path("cart", views.cart, name='cart'),
  path("shop", views.shop, name='shop'),
  path("blog", views.blog, name='blog'),
  path("contact", views.contact, name='contact'),
  path('login',views.login,name="login"),
  path('logout',views.logout,name="logout")

]
 