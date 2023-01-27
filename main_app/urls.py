from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
   path('', views.Home.as_view(), name="home"),
   path('about/', views.About.as_view(), name= 'about'),
   path('boybands/', views.BoyBandList.as_view(), name = 'boyband_list'),
   path('albums', views.AlbumList.as_view(), name='album_list'),
   path('boybands/new', views.BoyBandCreate.as_view(), name="boyband_create"),
   path('boybands/<int:pk>/', views.BoyBandDetail.as_view(), name="boyband_detail"),
   path('boybands/<int:pk>/update', views.BoyBandUpdate.as_view(), name= "boyband_update"),
   path('boybands/<int:pk>/delete', views.BoyBandDelete.as_view(), name = 'boyband_delete'),
]