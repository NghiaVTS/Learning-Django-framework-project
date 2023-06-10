from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('products/<product>', views.product_cat),
    path('submit', views.submit, name="submit"),
    path('submited', views.testing, name="submited"),
    path('submited_today', views.day_filter, name="submited_today"),
    path('aboutus', views.aboutUs, name="aboutUs"),
    path('services', views.services, name="services"),
    path('events', views.events, name="events"),
    path('menu', views.menu, name="menu"),
    path('diemden', views.diemden, name="diemden"),
    path('thuvien', views.thuvien, name="thuvien"),
    path('lienhe', views.lienhe, name="lienhe"),
]
