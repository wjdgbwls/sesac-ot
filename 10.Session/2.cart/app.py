from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)

app.secret_key ='abcd1234'

#상품 정보 등록
items ={
    'item1':{'name': '상품1','price':1000},
    'item2':{'name': '상품2','price':2000},
    'item3':{'name': '상품3','price':30000},
}
@app.route('/')
def index():
    return render_template('index.html',items=items)
@app.route('/add_to_cart/<item_name>')
def add_to_cart(item_name):
    if 'cart' not in session: #세션에 cart가 없으면 초기화 있으면 그냥진행
      session['cart'] = {}#장바구니에 담은 내용  
    #카트에 물건담기
    if item_name in session['cart']:
      session['cart'][item_name] += 1
    else:
      session['cart'][item_name] =1
    # 담은 이후 액션
    session.modified =True
    return redirect(url_for('index'))

@app.route('/view_cart')
def view_cart():
  total_price = 0
   #세션에서 카트 정보를 가져와서 출력한다.
  cart_items = session.get('cart', {})
  for item_name,item_info in cart_items.items():
    data=items.get(item_name)
    #이름 ,수량, 가격, 총가격
    #{}형태로 변환하고
    cart_items[item_name]={
      'name' : data['name'],
      'quantity' : item_info,
      'price' : data['price'],
      'sumprice' : data['price'] * item_info
    }
    total_price += (cart_items[item_name]['price']*cart_items[item_name]['quantity'])  # 각 상품 정보 출력

  return render_template('cart.html',cart_items=cart_items, total_price=total_price)
@app.route('/item_pop/<item_name>')
def item_pop(item_name):
  if 'cart' in session and item_name in session['cart']:
      session['cart'].pop(item_name)
      session.modified = True
  return redirect(url_for('view_cart'))
   
# 미션1, index.html 페이지에서, 상품명을 클릭해서 이 url이 호출되도록 구현하시오
# 미션 2 . 장바구니 보기 버튼 추가
# 미션 3 장바구니 내용을 세션을 통해 가져와서 cart.html 에 출력
if __name__ == '__main__':
    app.run(debug=True)