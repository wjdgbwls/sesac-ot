from django.urls import path
from . import views

urlpatterns= [
    path('login/', views.login_view, name='login'),
    path('home/',views.home_view, name ="home"),
    path('',views.hello_world, name = 'hello_world'),
    path('logout/',views.logout_view, name ='logout')
]