from flask import Flask, render_template, request
from config import app
from produk import *
from kategori import *

@app.route('/')
def index():
    products = getProducts()
    if 'idproduk' in request.args:
        id_produk = request.args['idproduk']
        product = getProductById(id_produk)
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
                            products = products
                            )

@app.route('/daftar')
def daftar():
    return render_template('daftar.html')

@app.route('/login')
def login():
    return render_template('login.html')

# @app.route('/kategori')
# def kategori():
#     return render_template('kategori.html')

@app.route('/keranjang')
def keranjang():
    return render_template('keranjang.html')

@app.route('/daftar-order')
def daftarOrder():
    return render_template('daftarorder.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

# @app.route('/produk')
# def produk():
#     return render_template('produk.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cari', methods=['GET', 'POST'])
def cari():
    if request.method == 'POST':
        produk = request.form['cari']
        data = searchProduct(produk)
        print produk
    return render_template('cari.html',
                            data = data
                            )

#------------------------------Admin Routing------------------------------

@app.route('/admin')
def admin():
    return render_template('adminIndex.html')

@app.route('/admin/manageorder')
def manageorder():
    return render_template('adminManageOrder.html')

@app.route('/admin/order')
def adminOrder():
    return render_template('adminOrder.html')

@app.route('/admin/kategori')
def adminKategori():
    return render_template('adminKategori.html')

@app.route('/admin/produk')
def adminProduk():
    return render_template('adminProduk.html')

@app.route('/admin/pembayaran')
def adminPembayaran():
    return render_template('adminPembayaran.html')

@app.route('/admin/customer')
def adminCustomer():
    return render_template('adminCustomer.html')

@app.route('/admin/user')
def adminUser():
    return render_template('adminUser.html')

#------------------------------Main------------------------------

if __name__ == "__main__":
    app.run(debug=True)