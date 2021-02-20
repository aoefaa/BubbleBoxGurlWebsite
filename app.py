from flask import Flask, render_template, request, session, redirect, url_for, flash
from config import app
from produk import *
from kategori import *
from verifikasi import *
from pembayaran import *
from user import *
from order import *
import os
from werkzeug.utils import secure_filename

@app.route('/', methods = ['GET','POST'])
def index():
    if len(session) == 0:
        if 'idproduk' in request.args:
            id_produk = request.args['idproduk']
            product = getProductById(id_produk)
            return render_template('produk.html',
                                    product = product
                                    )
        products = getProducts()
        return render_template('index.html',
                            categories = categories,
                            products = products,
                            
                            )
    else:
        nama = session['name']
        products = getProducts()
        if 'idproduk' in request.args:
            id_produk = request.args['idproduk']
            product = getProductById(id_produk)
            if request.method == 'POST':
                idproduk = request.form['idprod']
                userid = session['id']
                print idproduk, userid
            return render_template('produk.html',
                                    product = product
                                    )
        categories = getCategories()
        if 'idkategori' in request.args:
            id_kategori = request.args['idkategori']
            category = getCategory(id_kategori)
            product_by_category = getProductByCategory(id_kategori)

            if 'idproduk' in request.args:
                id_produk = request.args['idproduk']
                product = getProductById(id_produk)
                return render_template('produk.html',
                                        product = product
                                        )
            return render_template('kategori.html',
                                    category = category,
                                    categories = categories,
                                    product_by_category = product_by_category
                                    )
        return render_template('index.html',
                            categories = categories,
                            products = products,
                            nama = nama
                            )
    
    # return render_template('index.html',
    #                         categories = categories,
    #                         products = products
    #                         )

@app.route('/produk', methods=['GET', 'POST'])
def addCart():
    if request.method == 'POST':
        idproduk = request.form['idprod']
        print idproduk
        return redirect(url_for('keranjang'))

@app.route('/daftar')
def daftar():
    return render_template('daftar.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']
        arr = []
        arr.append(getEmail(email))
        if password == arr[0][0]['password']:
            session['id'] = arr[0][0]['userid']
            session['role'] = arr[0][0]['role']
            session['notelp'] = arr[0][0]['notelp']
            session['name'] = arr[0][0]['namalengkap']
            session['log'] = "Logged"
            return redirect(url_for('index'))
        
    return render_template('login.html')

@app.route('/keranjang')
def keranjang():
    userid = session['id']
    carts = getCartById(userid)
    count_carts = countCartByOrderId(carts[0]['orderid'])
    categories = getCategories()
    item_carts = getCartByOrderId(carts[0]['orderid'])
    return render_template('keranjang.html',
                            carts = carts,
                            count_carts = count_carts,
                            categories = categories,
                            item_carts = item_carts
                            )

@app.route('/checkout')
def checkout():
    nama = session['name']
    userid = session['id']
    carts = getCartById(userid)
    count_carts = countCartByOrderId(carts[0]['orderid'])
    categories = getCategories()
    item_carts = getCartByOrderId(carts[0]['orderid'])
    payments = getPayment()
    return render_template('checkout.html',
                            nama = nama,
                            count_carts = count_carts,
                            categories = categories,
                            item_carts = item_carts,
                            payments = payments
                            )

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/cari', methods=['GET', 'POST'])
def cari():
    if request.method == 'POST':
        searchForm = request.form['cari']
        item = searchProduct(searchForm)
        if len(item) == 0:
            products = getProducts()
            return render_template('cari.html',
                                    products = products
                                    )
    if 'idproduk' in request.args:
                id_produk = request.args['idproduk']
                product = getProductById(id_produk)
                return render_template('produk.html',
                                        product = product
                                        )
    return render_template('cari.html',
                            products = item
                            )

#------------------------------Admin Routing------------------------------

@app.route('/admin')
def admin():
    count_customers = countCustomers()
    count_order = countOrders()
    count_trans = countTransaction()
    return render_template('adminIndex.html',
                            count_customers = count_customers,
                            count_order = count_order,
                            count_trans = count_trans)

@app.route('/admin/manageorder')
def manageorder():
    orders = getOrders()
    if 'idorder' in request.args:
        id_order = request.args['idorder']
        order = getOrder(id_order)
        confirmation = getConfirmation(id_order)
        return render_template('adminOrder.html',
                                order = order,
                                confirmation = confirmation
                                )
    return render_template('adminManageOrder.html',
                            orders = orders,
                            )

@app.route('/admin/kategori')
def adminKategori():
    arr = []
    ac = []
    categories = getCategories()
    products = getProducts()
    for i in categories:
        count = countProductByCategory(i['idkategori'])
        arr.append(i)
        for j in count:
            ac.append(j)
    return render_template('adminKategori.html',
                            categories = categories,
                            acs = ac
                            )

@app.route('/admin/kategori', methods=['GET', 'POST'])
def addKategori():
    if request.method == 'POST':
        namakategori = request.form['namakategori']
        addCategory(namakategori)
        flash('Sukses')
    return redirect(url_for('adminKategori'))

UPLOAD_FOLDER = 'produk/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENTIONS = set(['png', 'jpg', 'jpeg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENTIONS

@app.route('/admin/produk', methods=['GET', 'POST'])
def adminProduk():
    products = getProductByIdCategory()
    categories = getCategories()
    if request.method == 'POST':
        # idkategori = request.form['idkategori']
        # namaproduk = request.form['namaproduk']
        # deskripsi = request.form['deskripsi']
        # rate = request.form['rate']
        # hargabefore = request.form['hargabefore']
        # hargaafter = request.form['hargaafter']
        # tgldibuat = request.form['namaproduk']
        gambar = request.files['uploadgambar']
        for i in gambar:
            if i and allowed_file(i.filename):
                filename = secure_filename(i.filename)
                b = i.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                print b
                # addProduct(filename)
        # print gambar
    return render_template('adminProduk.html',
                            products = products,
                            categories = categories)

@app.route('/admin/pembayaran')
def adminPembayaran():
    payments = getPayment()
    return render_template('adminPembayaran.html',
                            payments = payments)

@app.route('/admin/customer')
def adminCustomer():
    customers = getCustomers()
    return render_template('adminCustomer.html',
                            customers = customers)

@app.route('/admin/customer', methods=['GET', 'POST'])
def addCustomer():
    if request.method == 'POST':
        namalengkap = request.form['namalengkap']
        email = request.form['email']
        passw = request.form['password']
        notelp = request.form['notelp']
        alamat = request.form['alamat']
        role = 'Member'
        addUser(namalengkap, email, passw, notelp, alamat, role)
        flash('Sukses')
    return redirect(url_for('adminCustomer'))

@app.route('/admin/staff')
def adminStaff():
    staffs = getStaff()
    return render_template('adminUser.html',
                            staffs = staffs)

@app.route('/admin/staff', methods=['GET', 'POST'])
def addStaff():
    if request.method == 'POST':
        namalengkap = request.form['namalengkap']
        email = request.form['email']
        passw = request.form['password']
        notelp = request.form['notelp']
        alamat = request.form['alamat']
        role = 'Admin'
        addUser(namalengkap, email, passw, notelp, alamat, role)
        flash('Sukses')
    return redirect(url_for('adminStaff'))

#------------------------------Main------------------------------

if __name__ == "__main__":
    app.run(debug=True)