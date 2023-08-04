from django.urls import path
from photo_upload import views

urlpatterns = [
    path('upload/',views.photo_upload, name ='photo_upload'),
    path('list/',views.photo_list, name ='photo_list'),
]