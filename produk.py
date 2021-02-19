from flask import jsonify
from config import app, db 

def getProducts():
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM produk order by idproduk ASC")
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'idproduk':obj[0],'idkategori':obj[1],'namaproduk':obj[2],'gambar':obj[3],'deskripsi':obj[4],'rate':obj[5],'hargabefore':obj[6],'hargaafter':obj[7],'tgldibuat':obj[8]})
        count += 1
    return arr

def getProductById(id_produk):
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM produk where idproduk = '{0}'".format(id_produk))
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'idproduk':obj[0],'idkategori':obj[1],'namaproduk':obj[2],'gambar':obj[3],'deskripsi':obj[4],'rate':obj[5],'hargabefore':obj[6],'hargaafter':obj[7],'tgldibuat':obj[8]})
        count += 1
    return arr

def getProductByCategory(id_kategori):
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM produk where idkategori = '{0}'".format(id_kategori))
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'idproduk':obj[0],'idkategori':obj[1],'namaproduk':obj[2],'gambar':obj[3],'deskripsi':obj[4],'rate':obj[5],'hargabefore':obj[6],'hargaafter':obj[7],'tgldibuat':obj[8]})
        count += 1
    return arr

def searchProduct(namaproduk):
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM produk WHERE namaproduk LIKE '{0}'".format(namaproduk))
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'idproduk':obj[0],'idkategori':obj[1],'namaproduk':obj[2],'gambar':obj[3],'deskripsi':obj[4],'rate':obj[5],'hargabefore':obj[6],'hargaafter':obj[7],'tgldibuat':obj[8]})
        count += 1
    return arr