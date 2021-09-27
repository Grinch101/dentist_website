from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path('tables/', views.tables, name="tables"),
    path('register/', views.register, name="register"),
    path('password/', views.password, name="password"),
    path('login/', views.login, name="login"),
    path('layout_static/', views.layout_static, name="layout_static"),
    path('layout_sidenav_light/', views.layout_sidenav_light,
         name="layout_sidenav_light"),
    path('charts/', views.charts, name="charts")
]
