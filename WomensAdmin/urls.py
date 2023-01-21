from django.urls import path
from WomensAdmin import views

urlpatterns = [
    path('indexpage/',views.indexpage,name='indexpage'),
    path('addemployee/', views.addemployee, name='addemployee'),
    path('employeepage/', views.employeepage, name='employeepage'),
    path('displayemp/',views.displayemp,name='displayemp'),
    path('editdata/<int:dataid>/',views.editdata, name="editdata"),
    path('updatedata/<int:dataid>/', views.updatedata, name='updatedata'),
    path('deletedata/<int:dataid>/', views.deletedata, name='deletedata'),
    path('displaycategory/', views.displaycategory, name='displaycategory'),
    path('categorypage/', views.categorypage, name='categorypage'),
    path('viewcategory/', views.viewcategory, name='viewcategory'),
    path('editcategory/<int:dataid>/', views.editcategory, name="editcategory"),
    path('updatecategory/<int:dataid>/', views.updatecategory, name='updatecategory'),
    path('deletecategory/<int:dataid>/', views.deletecategory, name='deletecategory'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('productpage/', views.productpage, name='productpage'),
    path('viewproduct/', views.viewproduct, name='viewproduct'),
    path('editproduct/<int:dataid>/', views.editproduct, name="editproduct"),
    path('updateproduct/<int:dataid>/', views.updateproduct, name='updateproduct'),
    path('deleteproduct/<int:dataid>/', views.deleteproduct, name='deleteproduct'),
    path('deletecontact/<int:dataid>/', views.deletecontact, name='deletecontact'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('contactpages/',views.contactpages,name='contactpages')
]