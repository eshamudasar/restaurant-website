from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/LahoreBadshah"
app.secret_key = 'your_secret_key' 
mongo = PyMongo(app)
collection = mongo.db.menu

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
                    categories[category].append({'name': subitem['name'], 'price': subitem['price']})
    return render_template('menu.html', categories=categories.items())
cart=[]
@app.route('/cart', methods=['POST'])
def cart_handler():
    data = request.json
    item_id = data.get('item_id')
    item_name = data.get('item_name')
    item_price = data.get('item_price')

    if 'cart' not in session:
        session['cart'] = []

    item_exists = False
    for item in session['cart']:
        if item['id'] == item_id:
            item_exists = True
            item['quantity'] += 1
            break

    if not item_exists:
        session['cart'].append({'id': item_id, 'name': item_name, 'price': item_price, 'quantity': 1})
        session.modified = True

    # Return the updated cart item
    for item in session['cart']:
        if item['id'] == item_id:
            return jsonify({'quantity': item['quantity'], 'name': item['name'], 'price': item['price']})

    return jsonify({'quantity': 0})  # Return 0 if item not found

@app.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    data = request.json
    item_id = data.get('item_id')

    if 'cart' in session:
        session['cart'] = [item for item in session['cart'] if item['id']!= item_id]
        session.modified = True

    return jsonify(session['cart'])

@app.route('/cart')
def cart():
    if 'cart' in session:
        cart_items = session['cart']
    else:
        cart_items = []
    return render_template('cart.html', cart_items=cart_items)

@app.route('/checkout')
def checkout():
    session.pop('cart', None)
    return render_template('checkout.html')

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

@app.teardown_request
def teardown_request(exception):
    # Remove the cart only when the user checks out
    if request.path == '/checkout':
        session.pop('cart', None)

if __name__ == "__main__":
    app.run(debug=True)