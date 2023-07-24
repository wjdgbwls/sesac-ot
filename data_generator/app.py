from flask import Flask
from blueprints.user_info_blueprint import user_info_bp
from blueprints.store_blueprint import store_bp
from blueprints.user_blueprint import user_bp
from blueprints.item_blueprint import item_bp
from blueprints.orderItem_blueprint import orderItem_bp
from blueprints.order_blueprint import order_bp
from blueprints.kiosk_blueprint import kiosk_bp

app = Flask(__name__)

# 블루프린트 등록
app.register_blueprint(order_bp, url_prefix='/order')
app.register_blueprint(user_info_bp, url_prefix='/user')
app.register_blueprint(store_bp, url_prefix='/store')
app.register_blueprint(item_bp, url_prefix='/item')
app.register_blueprint(orderItem_bp, url_prefix='/orderitem')
app.register_blueprint(user_bp)
app.register_blueprint(kiosk_bp, url_prefix='/kiosk')

if __name__ == '__main__':
    app.run(host="0.0.0.0" , debug=True)