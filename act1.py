from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, template_folder='templates')
CORS(app)

@app.route('/home', methods=['GET'])
def index():
    return render_template('welcome.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/products', methods=['GET'])
def products():
    products = [
        {"id": 1, "name": "Iphone 20", "description": "Bitten Apple", "price": 10.99},
        {"id": 2, "name": "Samsung 100", "description": "Yummy 100", "price": 23.50},
        {"id": 3, "name": "Apple Orange", "description": "Healthy Living", "price": 7.25},
    ]
    return render_template('products.html', products=products)

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=7000)
