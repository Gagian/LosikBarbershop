from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('index',views.pelayan,name='index'),
    path('layanan',views.layanan,name='layanan'), 
    path('transaksi',views.transaksi,name='transaksi'),
    path('detaillayanan', views.detaillayanan,name='detaillayanan,'),
    path('createdatatransaksi', views.createdatatransaksi,name='createdatatransaksi'),
    path('createdatapelayan',views.createdatapelayan,name='createdatapelayan'),
    path('createdatalayanan',views.createdatalayanan,name='createdatalayanan'),
    path('updatepelayan/<str:id>',views.updatepelayan,name='updatepelayan'),
    path('updatelayanan/<str:id>',views.updatelayanan,name='updatelayanan'),
    path('updatetransaksi/<str:id>',views.updatetransaksi,name='updatetransaksi'),
    path('deletepelayan/<str:id>',views.deletepelayan,name='deletepelayan'),
    path('deletelayanan/<str:id>',views.deletelayanan,name='deletelayanan'),
    path('deletetransaksi/<str:id>',views.deletetransaksi,name='deletetransaksi')
]
