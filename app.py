from flask import Flask,request,render_template,session,redirect
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

cluster=MongoClient("mongodb+srv://amruthaarani0009:amrutha5005@clusteraws.fy0ng.mongodb.net/?retryWrites=true&w=majority&appName=Clusteraws")
db=cluster['bvc']
customers=db['customers']
uses=db['uses']
products=db['products']
carts=db['cart']
orders1=db['orders']

app=Flask(__name__)
app.secret_key="1234"

@app.route("/")
def home():
    return render_template("sample1.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/men-shirts")
def men_shirts():
    product=products.find({'productcategory':'men-shirts'})
    data=[]
    for i in product:
        dummy=[]
        dummy.append(i['_id'])
        dummy.append(i['imageurl'])
        dummy.append(i['productname'])
        data.append(dummy)
    return render_template("category-products.html", l=len(data), data=data, category_name="Men's Shirts")

@app.route("/men-pants")
def men_pants():
    product=products.find({'productcategory':'men-pants'})
    data=[]
    for i in product:
        dummy=[]
        dummy.append(i['_id'])
        dummy.append(i['imageurl'])
        dummy.append(i['productname'])
        data.append(dummy)
    return render_template("category-products.html", l=len(data), data=data, category_name="Men's Pants")

@app.route("/t-shirts")
def tshirts():
    product=products.find({'productcategory':'t-shirts'})
    data=[]
    for i in product:
        dummy=[]
        dummy.append(i['_id'])
        dummy.append(i['imageurl'])
        dummy.append(i['productname'])
        data.append(dummy)
    return render_template("category-products.html", l=len(data), data=data, category_name="T-Shirts")

@app.route("/women-dresses")
def women_dresses():
    product=products.find({'productcategory':'women-dresses'})
    data=[]
    for i in product:
        dummy=[]
        dummy.append(i['_id'])
        dummy.append(i['imageurl'])
        dummy.append(i['productname'])
        data.append(dummy)
    return render_template("category-products.html", l=len(data), data=data, category_name="Women's Dresses")

@app.route("/kids-wear")
def kids_wear():
    product=products.find({'productcategory':'kids-wear'})
    data=[]
    for i in product:
        dummy=[]
        dummy.append(i['_id'])
        dummy.append(i['imageurl'])
        dummy.append(i['productname'])
        data.append(dummy)
    return render_template("category-products.html", l=len(data), data=data, category_name="Kids Wear")

@app.route("/footwear")
def footwear():
    product=products.find({'productcategory':'footwear'})
    data=[]
    for i in product:
        dummy=[]
        dummy.append(i['_id'])
        dummy.append(i['imageurl'])
        dummy.append(i['productname'])
        data.append(dummy)
    return render_template("category-products.html", l=len(data), data=data, category_name="Footwear")

@app.route("/shorts")
def shorts():
    product=products.find({'productcategory':'shorts'})
    data=[]
    for i in product:
        dummy=[]
        dummy.append(i['_id'])
        dummy.append(i['imageurl'])
        dummy.append(i['productname'])
        data.append(dummy)
    return render_template("category-products.html", l=len(data), data=data, category_name="Shorts")

@app.route("/accessories")
def accessories():
    product=products.find({'productcategory':'accessories'})
    data=[]
    for i in product:
        dummy=[]
        dummy.append(i['_id'])
        dummy.append(i['imageurl'])
        dummy.append(i['productname'])
        data.append(dummy)
    return render_template("category-products.html", l=len(data), data=data, category_name="Accessories")

@app.route("/cart")
def cart():
    if 'username' not in session:
        return redirect("/")
    product=carts.find({'customer':session['username']})
    data=[]
    total_price=0
    for i in product:
        dummy=[]
        cart_product=products.find({'_id':ObjectId(i['product_id'])})
        for j in cart_product:
           total_price+=float(j['productprice'])*int(i['Qty'])
           dummy.append(j['imageurl'])
           dummy.append(j['productname'])
           dummy.append(j['productprice'])
           dummy.append(i['Qty'])
           dummy.append(j['productcolor'])
           dummy.append(j['productrating'])
           dummy.append(i['_id'])
           data.append(dummy)
    return render_template("cart.html",data=data,l=len(data),total_price=total_price)

@app.route("/customer-dashboard")
def customer_dashboard():
    if 'username' not in session:
        return redirect("/")
    return render_template("customer-dashboard.html")

@app.route("/customer-signup")
def customersingup():
    return render_template("customer-singup.html")

@app.route("/earnings")
def earnings():
    seller_email = session.get('username')
    if not seller_email:
        return redirect('/')

    seller_products = products.find({'owner': seller_email})
    seller_product_ids = [str(product['_id']) for product in seller_products]
    orders = orders1.find()

    total_earnings = 0
    pending_earnings = 0
    completed_sales = 0
    earnings_data = []

    for order in orders:
        order_total = 0
        for product in order['products']:
            if str(product['productid']) in seller_product_ids:
                order_total += product['total_price']
                
        if order_total > 0:
            earnings_data.append({
                'date': order['created_at'],
                'order_id': order['_id'],
                'products': [p for p in order['products'] if str(p['productid']) in seller_product_ids],
                'total': order_total,
                'status': order['status']
            })
            
            total_earnings += order_total
            
            if order['status'] == 'Delivered':
                completed_sales += 1
            else:
                pending_earnings += order_total

    return render_template('earnings.html', 
                         total_earnings=total_earnings, 
                         pending_earnings=pending_earnings, 
                         completed_sales=completed_sales,
                         earnings_data=earnings_data)

@app.route("/manage-products")
def manageproducts():
    if 'username' not in session:
        return redirect("/")
    seller_email = session.get('username')
    products_list = products.find({'owner': seller_email})
    data = []
    for product in products_list:
        item = []
        item.append(product['productname'])
        item.append(product['productcategory'])
        item.append(product['productprice'])
        item.append(product['productstock'])
        item.append(product['imageurl'])
        item.append(str(product['_id']))  # Convert ObjectId to string
        item.append(product.get('productdescription', ''))
        item.append(product.get('productcolor', ''))
        item.append(product.get('productrating', ''))
        item.append(', '.join(product.get('sizes', [])))  # Add sizes as comma-separated string
        data.append(item)
    return render_template("manage-products.html", data=data, l=len(data))

@app.route("/addproduct", methods=['post'])
def addproduct():
    if 'username' not in session:
        return redirect("/")
    productname=request.form.get("product-name")
    productcategory=request.form.get("product-category")
    productprice=request.form.get("product-price")
    productstock=request.form.get("product-stock")
    productdescription=request.form.get("product-description")
    productcolor=request.form.get("product-color")
    productrating=request.form.get("product-rating")
    imageurl=request.form.get("imageurl")
    productsizes=request.form.getlist("product-sizes")  # Get list of selected sizes
    
    products.insert_one({
        'productname':productname,
        'productcategory':productcategory,
        'productprice':productprice,
        'productstock':productstock,
        'productdescription':productdescription,
        'productcolor':productcolor,
        'productrating':productrating,
        'imageurl':imageurl,
        'sizes': productsizes,  # Add sizes to the product document
        'owner':session['username']
    })
    return redirect("/manage-products")

@app.route("/orders")
def orders():
    if 'username' not in session:
        return redirect("/")
    seller_email = session.get('username')
    seller_orders = []
    
    # Get all orders
    all_orders = orders1.find()
    # print(list(all_orders))
    
    for order in all_orders:
        # Check if any product in the order belongs to this seller
        seller_products = [p for p in order['products'] if products.find_one({'_id': ObjectId(p['productid']), 'owner': seller_email})]
        
        if seller_products:
            # Add seller-specific order info
            order_info = {
                'order_id': order['_id'],
                'customer_name': order['name'],
                'date': order['created_at'],
                'status': order['status'],
                'products': seller_products,
                'total_amount': order['total_amount']
            }
            seller_orders.append(order_info)
            
    return render_template("orders.html", orders=seller_orders)


@app.route("/order-details/<order_id>")
def order_details(order_id):
    print(order_id)
    if 'username' not in session:
        return redirect("/")
    try:
        # Only try to convert to ObjectId if it looks like a valid hex string
        if len(order_id) == 24 and all(c in '0123456789abcdefABCDEF' for c in order_id):
            order = orders1.find_one({'_id': ObjectId(order_id)})
            print(order)
            return render_template("order-details.html", order=order)
        else:
            return "Invalid order ID", 400
    except Exception as e:
        print(f"Error: {e}")
        return "Invalid order ID", 400

@app.route("/update-order-status/<order_id>", methods=['POST'])
def update_order_status(order_id):
    if 'username' not in session:
        return redirect("/")
    new_status = request.form.get('status')
    if new_status:
        orders1.update_one(
            {'_id': ObjectId(order_id)},
            {'$set': {'status': new_status}}
        )
    return redirect(f"/order-details/{order_id}")

@app.route("/seller-dashboard")
def sellerdashboard():
    if 'username' not in session:
        return redirect('/')
    return render_template("seller-dashboard.html")

@app.route("/seller-signup")
def sellersignup():
    return render_template("seller-signup.html")

@app.route("/selsignup1", methods=['post'])
def selsignup1():
    name=request.form.get("seller-name")
    email=request.form.get("seller-email")
    password=request.form.get("seller-password")
    user=uses.find_one({"Email":email})
    if(user):
        return render_template("seller-signup.html", status="Username Already Exists")
    uses.insert_one({"Name":name,"Email":email,"Password":password})
    return render_template("seller-signup.html", status="Registration Successful")

@app.route("/seller1-login")
def seller1login():
    return render_template("seller1-login.html")

@app.route("/selllogin1", methods=['post'])
def selllogin1():
    email=request.form.get("email")
    password=request.form.get("password")
    user=uses.find_one({"Email":email})
    if(user and user["Password"]==password):
        session['username']=email
        return redirect("/seller-dashboard")
    return render_template("seller1-login.html", result="Invalid Credentials")

@app.route("/customersignup1",methods=['post'])
def customersignup1():
    name=request.form.get("customername")
    email=request.form.get("customeremail")
    password=request.form.get("customerpassword")
    user=customers.find_one({"Email":email})
    if(user):
        return render_template("customer-singup.html", status="Username Already Exists")
    customers.insert_one({"Name":name,"Email":email,"Password":password})
    return render_template("customer-singup.html", status="Registration Successful")

@app.route("/clog",methods=['post'])
def clog():
    email=request.form.get("email")
    password=request.form.get("password")
    user=customers.find_one({"Email":email})
    if(user):
        if user["Password"]==password:
            session['username']=email
            return redirect("/customer-dashboard")
    return render_template("customer.html", result="Invalid Credentials")

@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect("/")

@app.route("/orderform", methods=['GET', 'POST'])
def orderform():
    if 'username' not in session:
        return redirect("/")

    if request.method == 'POST':
        cart_items = carts.find({'customer': session['username']})
        order_products = []
        total_amount = 0

        for cart_item in cart_items:
            product = products.find_one({'_id': ObjectId(cart_item['product_id'])})
            if product:
                quantity = int(cart_item['Qty'])
                price = float(product['productprice'])
                total_price = quantity * price

                order_products.append({
                    'productid': cart_item['product_id'],
                    'quantity': quantity,
                    'price': price,
                    'total_price': total_price,
                    'name': product['productname']
                })

                total_amount += total_price

                # Update product stock
                new_stock = int(product['productstock']) - quantity
                products.update_one(
                    {'_id': ObjectId(cart_item['product_id'])},
                    {'$set': {'productstock': str(new_stock)}}
                )

        # Get user input from the form
        name = request.form.get('name')
        phone = request.form.get('phone')
        address = request.form.get('address')

        order = {
            'email': session['username'],
            'name': name,
            'phone': phone,
            'address': address,
            'products': order_products,
            'total_amount': total_amount,
            'status': 'Pending',
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        result = orders1.insert_one(order)

        # Clear cart after placing order
        carts.delete_many({'customer': session['username']})

        return redirect(f"/order-confirmation/{result.inserted_id}")

    return render_template("orderform.html")

@app.route("/order-confirmation/<order_id>")
def order_confirmation(order_id):
    order = orders1.find_one({'_id': ObjectId(order_id)})
    return render_template("order-confirmation.html", order=order,)

@app.route("/my-orders")
def my_orders():
    if 'username' not in session:
        return redirect("/")
    customer_orders = orders1.find({'email': session['username']})
    return render_template("customer-orders.html", orders=customer_orders)

@app.route("/addtocart/<product_id>")
def addtocart(product_id):
    if 'username' not in session:
        return redirect("/")
    
    Qty = request.args.get('Qty', 1)
    
    cart_item = {
        'customer': session['username'],
        'product_id': product_id,
        'Qty': Qty
    }
    
    carts.insert_one(cart_item)
    return redirect("/cart")

@app.route("/deletecart/<product_id>", methods=['POST'])
def delete_product_cart(product_id):
    carts.delete_one({'_id': ObjectId(product_id)})
    return redirect("/cart")


@app.route("/edit-product/<product_id>", methods=['GET', 'POST'])
def edit_product(product_id):
    if 'username' not in session:
        return redirect("/")
    
    if request.method == 'POST':
        products.update_one(
            {'_id': ObjectId(product_id)},
            {'$set': {
                'productname': request.form.get('productname'),
                'productcategory': request.form.get('productcategory'),
                'productprice': request.form.get('productprice'),
                'productstock': request.form.get('productstock'),
                'imageurl': request.form.get('imageurl'),
                'productdescription': request.form.get('productdescription'),
                'productcolor': request.form.get('productcolor'),
                'productrating': request.form.get('productrating')
            }}
        )
        return redirect("/manage-products")
    
    product = products.find_one({'_id': ObjectId(product_id)})
    return render_template("edit-product.html", product=product)

@app.route("/deleteproduct/<product_id>", methods=['POST'])
def delete_product(product_id):
    if 'username' not in session:
        return redirect("/")
    products.delete_one({'_id': ObjectId(product_id)})
    return redirect("/manage-products")

@app.route("/profile")
def profile():
    if 'username' not in session:
        return redirect("/")
    
    user_data = uses.find_one({'Email': session['username']})

    if user_data:
        # Ensure all necessary fields exist
        user_data.setdefault('phone', 'Not Available')
        user_data.setdefault('address', 'Not Available')

    return render_template("profile.html", user=user_data)

from flask import request, redirect, flash

@app.route("/update-profile", methods=["POST"])
def update_profile():
    if 'username' not in session:
        return redirect("/")

    # Get form data
    name = request.form.get("name")
    phone = request.form.get("phone")
    address = request.form.get("address")

    # Ensure user exists
    user_email = session['username']
    user_data = uses.find_one({"Email": user_email})

    if not user_data:
        flash("User not found!", "error")
        return redirect("/profile")

    # Update user details in the database
    update_data = {
        "Name": name,
        "phone": phone,
        "address": address
    }
    uses.update_one({"Email": user_email}, {"$set": update_data})

    flash("Profile updated successfully!", "success")
    return redirect("/profile")


@app.route("/support")
def support():
    if 'username' not in session:
        return redirect("/")
    return render_template("support.html")

@app.route("/view-product/<product_id>")
def view_product(product_id):
    if 'username' not in session:
        return redirect("/")
    product = products.find_one({'_id': ObjectId(product_id)})
    if not product:
        return redirect("/products")
    return render_template("view-product.html", product=product)



@app.route("/customer")
def customer():
    return render_template("customer.html")

@app.route("/customer-singup")
def customer_signup():
    return render_template("customer-singup.html")

@app.route("/products")
def view_products():
    if 'username' not in session:
        return redirect("/")
    all_products = products.find()
    data = []
    for product in all_products:
        item = []
        item.append(product['productname'])
        item.append(product['productcategory'])
        item.append(product['productprice'])
        item.append(product.get('productstock', ''))
        item.append(product['imageurl'])
        item.append(str(product['_id']))
        item.append(product.get('productdescription', ''))
        item.append(product.get('productcolor', ''))
        item.append(product.get('productrating', ''))
        item.append(', '.join(product.get('sizes', [])))
        data.append(item)
    return render_template("products.html", data=data, l=len(data))

if __name__=="__main__":
    app.run(port=5000,host="0.0.0.0",debug=True)
