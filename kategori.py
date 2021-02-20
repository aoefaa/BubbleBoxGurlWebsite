from flask import jsonify
from config import app, db

def getCategories():
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM kategori order by namakategori ASC")
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'idkategori':obj[0],'namakategori':obj[1],'tgldibuat':obj[2]})
        count += 1
    return arr

def getCategory(id_kategori):
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT * FROM kategori WHERE idkategori = '{0}'".format(id_kategori))
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'idkategori':obj[0],'namakategori':obj[1],'tgldibuat':obj[2]})
        count += 1
    return arr

def getIdCategory():
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT idkategori FROM kategori")
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'idkategori':obj[0]})
        count += 1
    return arr

def countProductByCategory(id_kategori):
    arr = []
    cur = db.connection.cursor()
    cur.execute("SELECT Count(idproduk) AS count FROM produk p, kategori k where p.idkategori=k.idkategori and k.idkategori='{0}' order by idproduk ASC".format(id_kategori))
    data = cur.fetchall()
    count = 0
    while(count < len(data)):
        obj = data[count]
        arr.append({'count':obj[0]})
        count += 1
    return arr
    