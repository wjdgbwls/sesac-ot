from django.shortcuts import render, redirect
from .models import User
from .models import Item

def user_register(request):
    if request.method == 'POST':
      name = request.POST['name']
      number = request.POST['phonenumber']
      User.objects.create(name = name, phonenumber = number)
      return redirect('home')
    return render(request, 'petapp/user_register.html' )

def home(request):
   return render(request, 'petapp/home.html')

def user_list(request):
  users = User.objects.all()
  # 템플릿에서 사용할 변수명과 데이터를 딕셔너리로 묶어서 보냄
  return render(request, 'petapp/user_list.html',{'users': users})

def item_list(request):
   items = Item.objects.all()
   return render(request, 'petapp/item.html',{'items': items} )
