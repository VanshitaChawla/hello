from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    
  path("", views.ecom, name='ecom')  ,
  path("about", views.about, name='about') , 
  path("cart", views.cart, name='cart'),
  path("shop", views.shop, name='shop'),
  path("blog", views.blog, name='blog'),
   path("product/<int:id>", views.product, name='product'),
  path("contact", views.contact, name='contact'),
  path('login',views.login,name="login"),
  path('logout',views.logout,name="logout"),
  path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
  path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

  path('Check_out_cart/<int:total>/', views.Check_out_cart, name='Check_out_cart'),
]
 