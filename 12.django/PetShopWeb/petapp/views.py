from django.shortcuts import render, redirect
from .models import User
from .models import Item
from .models import MainImg

#유저를 등록합니다.
def user_register(request):
    if request.method == 'POST':
      name = request.POST['name']
      number = request.POST['phonenumber']
      User.objects.create(name = name, phonenumber = number)
      return redirect('home')
    return render(request, 'petapp/user_register.html' )

#메인 홈페이지를 띄워줍니다
def home(request):
   img = MainImg.objects.all()
   return render(request, 'petapp/home.html',{'img': img})

#유저 리스트를 확인할 수 있습니다 이것은 확인하기 위한 용
def user_list(request):
  users = User.objects.all()
  # 템플릿에서 사용할 변수명과 데이터를 딕셔너리로 묶어서 보냄
  return render(request, 'petapp/user_list.html',{'users': users})

#아이템 리스트를 홈페이지에 표시합니다.
def item_list(request):
   items = Item.objects.all()
   return render(request, 'petapp/item.html',{'items': items} )

   