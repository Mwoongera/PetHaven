from flask import *
import pymysql
def db_connection():
    return pymysql.connect(host='localhost', user='root', password='', database='pet_haven')

# Start
app = Flask(__name__)
app.secret_key = "12345678"

# Login
@app.route('/login', methods = ['POST', 'GET'])
def login():
 if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    connection = db_connection()
    cursor = connection.cursor()
    sql = "select * from users where email = %s and password = %s"
    data = (username, password)
    cursor.execute(sql, data)

    count = cursor.rowcount
    if count == 0:
        return render_template('login.html', message1 = 'Invalid Credentials')

    else:
        user = cursor.fetchone()
        session['key'] = user[1]
    return redirect('/')

 else:
    return render_template('login.html', message2 = 'Login Here' )

# Sign Up
@app.route('/signup', methods = ['POST', 'GET'])
def register():
      if request.method == 'POST':
          username = request.form["username"]
          email = request.form["email"]
          password = request.form["password"]
          confirm = request.form["confirm"]
          phone = request.form["phone"]
          
          import pymysql
          connection = pymysql.connect(host = 'localhost', user = 'root', password='', database='pet_haven')
          
          cursor = connection.cursor()
          data = (username, email,password, phone)
          sql = "insert into users (username, email, password, phone) values(%s, %s, %s, %s)"
          
          if password != confirm:
              return render_template('register.html', warning = 'Password doesnt Match!')
          elif len(password) <8:
           return render_template('register.html', warning = 'Password is less than 8 characters')
          
          else:
              cursor.execute(sql, data)
              connection.commit()
              return render_template('signup.html', success = 'Registred Succesfully')
            
      else:
          return render_template('signup.html', message = 'Please Add Your Information')

# Home Route
@app.route('/')
def home():
    return render_template('index.html')

# Upload Product
@app.route('/upload', methods = ['POST', 'GET' ])
def upload():
         if request.method == 'POST':
        # capture data from the form: name
            product_name = request.form['product_name']
            product_desc= request.form['product_desc']
            product_cost= request.form['product_cost']
            product_category= request.form['product_category']
        # files in your computer
            product_image1= request.files['product_image1']

        # save the three iamges in your application
        # static/images
            product_image1.save('petimages' + product_image1.filename)

        #  Database connection and cursor()
            connection = db_connection()
            cursor = connection.cursor()

        # sql: to insert a product record
            sql = """insert into products (product_name, product_desc, product_cost, product_category, product_image1) values (%s, %s, %s, %s, %s)"""
            data = (product_name, product_desc, product_cost, product_category, product_image1.filename)
            cursor.execute(sql, data)
            connection.commit()
            return render_template('upload.html', message1 = 'Product Added Successfully.')
        
         else:
             return render_template('upload.html', message2 = "Please Add Products!")

# Products Route
@app.route('/products')
def products():
    return render_template('products.html')

# New Products Route
@app.route('/newproducts')
def new():
    return render_template('newproducts.html')

# Services Route
@app.route('/services')
def services():
    return render_template('services.html')

# FAQ Route
@app.route('/faq' , methods = ['POST','GET'])
def faq():
    return render_template('faq.html')

# Adopt a Pet Route
@app.route('/adoption')
def adoption():
    return render_template('adoption.html')

# See All
@app.route('/dogs')
def dogs():
    return render_template('dogs.html')

@app.route('/dogfood')
def dogfood():
    return render_template('dogfood.html')

@app.route('/cats')
def cats():
    return render_template('cats.html')

@app.route('/catfood')
def catfood():
    return render_template('catfood.html')

@app.route('/birds')
def birds():
    return render_template('birds.html')

@app.route('/birdfood')
def birdfoood():
    return render_template('birdfood.html')

@app.route('/fish')
def fish():
    return render_template('fish.html')

@app.route('/fishfood')
def fishfood():
    return render_template('fishfood.html')

@app.route('/hamsters')
def hamsters():
    return render_template('hamsters.html')

@app.route('/hamsterfood')
def hamsterfood():
    return render_template('hamsterfood.html')

# Adopt
@app.route('/adopt')
def adopt():
    return render_template('adopt.html')


# Cart
@app.route('/cart')
def cart():
    return render_template('cart.html')

# Pet Care Route
@app.route('/care' , methods = ['POST' ])
def care():
    return render_template('care.html')

# Events Route
@app.route('/events')
def events():
    return render_template('events.html')

# Blog Route
@app.route('/blog' , methods = ['POST', 'GET'])
def blog():
    return render_template('blog.html')



app.run(debug=True)
# Stop
