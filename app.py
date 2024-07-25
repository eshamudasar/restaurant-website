from flask import Flask, render_template, request, session, jsonify
from flask_pymongo import PyMongo
import uuid
from flask_session import Session

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://admin:admin@mycluster.w4b9g4s.mongodb.net/LahoreBadshah"
app.secret_key = 'your_secret_key' 
mongo = PyMongo(app)
collection = mongo.db.menu

app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def index():
    featured_dishes = [
        {'name': 'Chicken Curry', 'description': 'A classic Pakistani dish', 'price': 7.00, 'image_file': 'Chicken_Curry.jpg'},
        {'name': 'Lamb Curry', 'description': 'Our signature dish', 'price': 8.50, 'image_file': 'Lamb_Karahi.jpg'},
        {"name": "Seekh Kebab", "price": "6.00", "image_file": "seekh_kabab.jpg", "description": "Tender and flavorful seekh kebab served with a side of mint chutney", "calories": 250, "spice_level": "mild"},
        {"name": "Lamb Chops", "price": "8.50", "image_file": "lamb_chops.jpg", "description": "Tender and juicy lamb chops served with a side of garlic sauce", "calories": 350, "spice_level": "medium"},
        {"name": "Chicken Wings", "price": "5.00", "image_file": "chicken_wings.jpg", "description": "Crispy fried chicken wings served with a side of BBQ sauce", "calories": 200, "spice_level": "mild"},
        {"name": "Lamb Tikka", "price": "8.00", "image_file": "lamb_tikka.jpg", "description": "Tender and flavorful lamb tikka served with a side of mint chutney", "calories": 250, "spice_level": "mild"},
        {"name": "Chicken Tikka", "price": "6.00", "image_file": "chicken_tikka.jpg", "description": "Tender and flavorful chicken tikka served with a side of mint chutney", "calories": 200, "spice_level": "mild"},
        {"name": "Malai Botti", "price": "6.00", "image_file": "malai_botti.jpg", "description": "Tender and flavorful malai botti served with a side of mint chutney", "calories": 250, "spice_level": "mild"},
        {"name": "Mixed Grill", "price": "18.00", "image_file": "mixed_grill.jpg", "description": "A combination of lamb, chicken, and fish served with a side of herbs", "calories": 500, "spice_level": "medium"}
      
    ]
    return render_template('index.html', featured_dishes=featured_dishes)


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
                if '_id' not in subitem:
                    subitem['_id'] = str(uuid.uuid4())
                categories[category].append({
                    'id': str(subitem['_id']),  # Ensure '_id' is converted to a string
                    'name': subitem['name'],
                    'price': subitem['price'],
                    'image_file': subitem['image_file']
                })
    return render_template('menu.html', categories=categories.items())

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
        session['cart'][item_id] = {
            'name': item_name,
            'price': item_price,
            'quantity': 1
        }
    session.modified = True
    return jsonify({'quantity': session['cart'][item_id]['quantity']})

@app.route('/cart/update', methods=['POST'])
def update_quantity():
    item_id = request.json['item_id']
    quantity = int(request.json['quantity'])
    if 'cart' in session and item_id in session['cart']:
        session['cart'][item_id]['quantity'] = quantity
    session.modified = True
    return jsonify({})

@app.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    if 'cart' in session:
        item_id = request.json['item_id']
        if item_id in session['cart']:
            del session['cart'][item_id]
            session.modified = True
            subtotal = sum(float(item['price']) * item['quantity'] for item in session['cart'].values())
            return jsonify({'subtotal': subtotal})
    return jsonify({'error': 'Item not found in cart'}), 404

@app.route('/cart')
def cart():
    if 'cart' in session:
        cart_items = list(session['cart'].values())
        item_ids = list(session['cart'].keys())
        cart_list = [{'item': item, 'item_id': item_id} for item, item_id in zip(cart_items, item_ids)]
        subtotal = sum(float(item['price']) * item['quantity'] for item in cart_items)
        total = subtotal
    else:
        cart_list = []
        subtotal = 0
        total = 0
    return render_template('cart.html', cart_list=cart_list, subtotal=subtotal, total=total)


@app.route('/checkout')
def checkout():
    if 'cart' in session:
        cart_items = session['cart']
        subtotal = sum(float(item['price'].replace('£', '').replace(',', '')) * item['quantity'] for item in cart_items.values())
        total = subtotal
    else:
        cart_items = {}
        subtotal = 0
        total = 0
    return render_template('checkout.html', cart_items=cart_items, subtotal=subtotal, total=total)

@app.route('/checkout/process', methods=['POST'])
def process_checkout():
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
