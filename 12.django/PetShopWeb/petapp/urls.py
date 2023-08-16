from django.urls import path
from petapp import views

urlpatterns= [
    path('register/', views.user_register, name='user'),

    #홈 화면으로
    path('', views.home , name ='home'),

    #user db의 내용을표시
    path('userlist/',views.user_list, name ='list'),

    #item 목록
    path('item/', views.item_list, name = 'item'),
]