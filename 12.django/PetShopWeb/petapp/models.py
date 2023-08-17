from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200) # 유저의 이름을 저장
    phonenumber = models.TextField(default='') # 유저의 폰을 저장

class Item(models.Model):
    title = models.CharField(max_length=100)  # 상품 제목을 저장하는 필드
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 상품 가격을 저장하는 필드
    img = models.ImageField(upload_to='items/')  #이미지를 저장하는 필드

class MainImg(models.Model):
    title = models.CharField(max_length = 100)
    img = models.ImageField(upload_to='mainimgs/')



    def __str__(self):
        return f"타이틀:{self.title}"