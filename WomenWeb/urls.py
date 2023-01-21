from django.urls import path
from WomenWeb import views

urlpatterns=[
path('', views.mylogin, name='mylogin'),
    path('mainpage/',views.mainpage,name='mainpage'),
    path('Contactpage/',views.Contactpage,name='Contactpage'),
    path('savedata/',views.savedata,name='savedata'),
    path('Aboutpage/', views.Aboutpage, name='Aboutpage'),
    path('catpage/<itemCatg>', views.catpage, name='catpage'),
    path('productdetails/<int:dataid>', views.productdetails, name='productdetails'),
    path('cart/', views.cart, name='cart'),
    path('cartsave/',views.cartsave,name='cartsave'),
    path('deletecart/<int:dataid>/',views.deletecart,name='deletecart'),
    path('billingpage/', views.billingpage, name='billingpage'),
    path('savebilling/', views.savebilling, name='savebilling'),

    path('regdata/',views.regdata,name='regdata'),
    path('customerlogin/',views.customerlogin,name='customerlogin'),
    path('userlogout/',views.userlogout,name='userlogout')
]