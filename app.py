from flask import Flask, render_template, request, session, jsonify
from flask_pymongo import PyMongo
import uuid
from flask_session import Session

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/LahoreBadshah"
app.secret_key = 'your_secret_key' 
mongo = PyMongo(app)
collection = mongo.db.menu

app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    menu_items = collection.find()
    categories = {}
    for item in menu_items:
        if 'category' in item and 'items' in item:
            category = item['category']
            if category not in categories:
                categories[category] = []
                for subitem in item['items']:
                    categories[category].append({'name': subitem['name'], 'price': subitem['price'], 'image_file': subitem['image_file']})
    return render_template('menu.html', categories=categories.items())

cart=[]
@app.route('/cart', methods=['POST'])
def add_to_cart():
    if 'cart' not in session:
        session['cart'] = {}
    item_id = request.json['item_id']
    item_name = request.json['item_name']
    item_price = request.json['item_price']
    if item_id in session['cart']:
        session['cart'][item_id]['quantity'] += 1
    else:
        session['cart'][item_id] = {'name': item_name, 'price': item_price, 'quantity': 1}
    return jsonify({'quantity': session['cart'][item_id]['quantity']})

@app.route('/cart/update', methods=['POST'])
def update_quantity():
    item_id = request.json['item_id']
    quantity = int(request.json['quantity'])
    if 'cart' in session and item_id in session['cart']:
        session['cart'][item_id]['quantity'] = quantity
    return jsonify({})

@app.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    item_id = request.json['item_id']
    if 'cart' in session and item_id in session['cart']:
        del session['cart'][item_id]
    return jsonify({})

@app.route('/cart')
def cart():
    if 'cart' in session:
        cart_items = session['cart']
        subtotal = sum(float(item['price'].replace('£', '').replace(',', '')) * item['quantity'] for item in cart_items.values())
        total = subtotal
    else:
        cart_items = {}
        subtotal = 0
        total = 0
    return render_template('cart.html', cart_items=cart_items, subtotal=subtotal, total=total)

@app.route('/checkout', methods=['POST'])
def checkout():
    order_id = uuid.uuid4().hex
    # Process payment and create order
    return jsonify({'orderId': order_id})

@app.route('/reservation')
def reservation():
    return render_template('reservation.html')

@app.route('/catering')
def catering():
    return render_template('catering.html')

@app.route('/careers')
def careers():
    return render_template('careers.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
