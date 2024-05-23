from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = "390ccbf61aa82533c12e8c6c1d2eb1dc"

# Product service URL
product_service_url = 'http://172.20.0.3:8080/products'
product_service_init_url = 'http://172.20.0.3:8080//product-create'

# Authentication service URL
auth_service_url_for_login = 'http://172.20.0.5:5000/api/login'
auth_service_url_for_register = 'http://172.20.0.5:5000/api/register'


cart_service_url_for_addtocart='http://172.20.0.4:3000//cart/add'
cart_service_url_for_viewcart='http://172.20.0.4:3000//cart'


@app.route('/home')
def home():
    # Fetch products from product service
    products_response = requests.get(product_service_url)
    print(products_response)
    products = products_response.json()
    print("Products returned in response:", products)
    return render_template('home.html', products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Extract username and password from the form data
        username = request.form['username']
        password = request.form['password']

        data = {
            "username": username,
            "password": password

        }
        auth_response = requests.post(auth_service_url_for_login, json=data)
        print("this is statucode", auth_response.status_code)

        if auth_response.status_code == 200:
            flash('Registration successful! You can now log in.', 'success')
            print("Successsssssssssssssssssssssssssssssss")
            new_product = {
                "id":123,
                "name": "Iphone15 Pro Max",
                "description": "Phone of 2024",
                "category": "Phones",
                "weight": 220.5,
                "dimension": "13*14",
                "price": 4300
            }

            auth_response2=requests.post(product_service_init_url,json=new_product)
            print("this is the response of addind product",auth_response2.json)
            if auth_response2.status_code==201:
                print("added successfully")

            return redirect(url_for('home'))
        else:
            # Authentication failed, display error message

            error_message = 'Invalid username or password. Please try again.'
            print(error_message)
            return render_template('login.html', error_message=error_message)
    else:
        return render_template('login.html')

@app.route('/')
@app.route('/register', methods=['Get','POST'])
def register():
    if request.method == 'POST':
        # Extract username and password from the form data
        username = request.form['username']
        password = request.form['password']
        email=request.form['email']
        data = {
            "username": username,
            "password": password,
            "email":email
        }
        auth_response = requests.post(auth_service_url_for_register, json=data)
        print("this is statucode",auth_response.status_code)
        print(auth_service_url_for_register)
        if auth_response.status_code==201 :
            flash('Registration successful! You can now log in.', 'success')
            print("Successsssssssssssssssssssssssssssssss")
            return redirect(url_for('login'))
        else:
            # Authentication failed, display error message

            error_message = 'Invalid username or password. Please try again.'
            print(error_message)
            return render_template('register.html', error_message=error_message)
    else:
        return render_template('register.html')

@app.route('/cart', methods=['Get','POST'])
def cart():
        productname = request.form['productname']
        price = request.form['productprice']
        quantity=1
        data = {
            "product_name": productname,
            "price": price,
            "quantity": quantity
        }
        auth_response = requests.post(cart_service_url_for_addtocart, json=data)
        print(auth_response.status_code)
        if auth_response.status_code==201:
            print("Added successfull")

        products_response = requests.get(product_service_url)
        print(products_response)
        products = products_response.json()
        print("Products returned in response:", products)
        return render_template('home.html', products=products)
@app.route('/viewcart')
def viewcart():
    products_response = requests.get(cart_service_url_for_viewcart)
    print(products_response)
    carts = products_response.json()
    print("Products returned in response:", carts)
    return render_template('cart.html', cart=carts['cart_items'])

if __name__ == '__main__':
    app.run(debug=True,port=4000,host='0.0.0.0')